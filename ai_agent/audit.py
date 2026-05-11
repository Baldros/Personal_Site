"""Persistent audit log for Atlas conversations."""

from __future__ import annotations

import json
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
HISTORY_DIR = PROJECT_ROOT / "History"
DB_PATH = HISTORY_DIR / "atlas_audit.sqlite3"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _connect() -> sqlite3.Connection:
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.execute("PRAGMA journal_mode=WAL")
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS audit_events (
            event_id TEXT PRIMARY KEY,
            thread_id TEXT NOT NULL,
            turn_id INTEGER,
            role TEXT,
            event_type TEXT NOT NULL,
            content TEXT,
            metadata_json TEXT NOT NULL DEFAULT '{}',
            created_at TEXT NOT NULL
        )
        """
    )
    connection.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_audit_events_thread_created
        ON audit_events(thread_id, created_at)
        """
    )
    return connection


def record_event(
    thread_id: str,
    event_type: str,
    *,
    role: str | None = None,
    content: str | None = None,
    turn_id: int | None = None,
    metadata: dict[str, Any] | None = None,
) -> str:
    """Record a single auditable event and return its id."""
    event_id = str(uuid.uuid4())
    created_at = utc_now()
    payload = json.dumps(metadata or {}, ensure_ascii=False, default=str)

    with _connect() as connection:
        connection.execute(
            """
            INSERT INTO audit_events (
                event_id, thread_id, turn_id, role, event_type,
                content, metadata_json, created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                event_id,
                thread_id,
                turn_id,
                role,
                event_type,
                content,
                payload,
                created_at,
            ),
        )

    return event_id


def record_message(
    thread_id: str,
    role: str,
    content: str,
    *,
    turn_id: int | None = None,
    metadata: dict[str, Any] | None = None,
) -> str:
    return record_event(
        thread_id,
        "message",
        role=role,
        content=content,
        turn_id=turn_id,
        metadata=metadata,
    )


def export_thread_json(thread_id: str, messages: list[dict[str, Any]]) -> Path:
    """Write a human-readable transcript beside the SQLite audit database."""
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    transcript_path = HISTORY_DIR / f"chat_{thread_id}.json"
    transcript = {
        "thread_id": thread_id,
        "exported_at": utc_now(),
        "messages": messages,
    }
    transcript_path.write_text(
        json.dumps(transcript, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    return transcript_path


def get_thread_events(thread_id: str) -> list[dict[str, Any]]:
    with _connect() as connection:
        rows = connection.execute(
            """
            SELECT event_id, thread_id, turn_id, role, event_type,
                   content, metadata_json, created_at
            FROM audit_events
            WHERE thread_id = ?
            ORDER BY created_at ASC
            """,
            (thread_id,),
        ).fetchall()

    return [
        {
            "event_id": event_id,
            "thread_id": row_thread_id,
            "turn_id": turn_id,
            "role": role,
            "event_type": event_type,
            "content": content,
            "metadata": json.loads(metadata_json or "{}"),
            "created_at": created_at,
        }
        for (
            event_id,
            row_thread_id,
            turn_id,
            role,
            event_type,
            content,
            metadata_json,
            created_at,
        ) in rows
    ]
