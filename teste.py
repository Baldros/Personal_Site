#!/usr/bin/env python3
"""
list_repos.py

Lista todos os repositórios (públicos de um usuário ou todos do usuário autenticado).
- Para repositórios privados/colaborações use GITHUB_TOKEN e --private
- Segue paginação via header 'Link'
- Trata rate limits básicos e erros transitórios
"""

import os
import time
import argparse
import requests
import sys
import csv
import json

API_BASE = "https://api.github.com"
PER_PAGE = 100  # máximo permitido

def get(url, headers, params):
    tries = 0
    backoff = 1
    while tries < 5:
        r = requests.get(url, headers=headers, params=params)
        # Rate limit handling
        if r.status_code == 403 and r.headers.get("X-RateLimit-Remaining") == "0":
            reset = int(r.headers.get("X-RateLimit-Reset", 0))
            wait = max(0, reset - int(time.time()) + 2)
            print(f"Rate limit atingido. Aguardando {wait} segundos até o reset...", file=sys.stderr)
            time.sleep(wait)
            tries += 1
            continue
        if r.status_code in (500, 502, 503, 504):
            time.sleep(backoff)
            backoff *= 2
            tries += 1
            continue
        r.raise_for_status()
        return r
    r.raise_for_status()
    return r

def iter_repos(url, headers, params):
    while url:
        r = get(url, headers, params)
        data = r.json()
        for i in data:
            yield i
        # parse Link header
        link = r.headers.get("Link", "")
        next_url = None
        if link:
            parts = link.split(",")
            for p in parts:
                if 'rel="next"' in p:
                    # <https://api.github.com/...?page=2>; rel="next"
                    next_url = p[p.find("<")+1:p.find(">")]
                    break
        if next_url:
            url = next_url
            params = None  # já embutido em next_url
        else:
            break

def format_markdown(repos):
    lines = ["| Nome | Visibilidade | Descrição | URL |", "|---|---:|---|---|"]
    for r in repos:
        name = r.get("name")
        vis = "private" if r.get("private") else "public"
        desc = (r.get("description") or "").replace("\n", " ").replace("|", "\\|")
        html = r.get("html_url")
        lines.append(f"| `{name}` | {vis} | {desc} | [{html}]({html}) |")
    return "\n".join(lines)

def main():
    p = argparse.ArgumentParser(description="Listar repositórios GitHub (públicos ou de usuário autenticado).")
    p.add_argument("--owner", "-o", default="Baldros", help="Nome do usuário (para listar públicos via /users/OWNER/repos).")
    p.add_argument("--private", action="store_true", help="Use /user/repos (requer GITHUB_TOKEN) para incluir privados/colaborações.")
    p.add_argument("--format", "-f", choices=["markdown", "json", "csv"], default="markdown", help="Formato de saída.")
    args = p.parse_args()

    token = os.getenv("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"

    if args.private:
        if not token:
            print("Erro: --private requer GITHUB_TOKEN no ambiente.", file=sys.stderr)
            sys.exit(1)
        url = f"{API_BASE}/user/repos"
        params = {"per_page": PER_PAGE, "affiliation": "owner,collaborator,organization_member"}
    else:
        url = f"{API_BASE}/users/{args.owner}/repos"
        params = {"per_page": PER_PAGE, "type": "all"}

    repos = list(iter_repos(url, headers, params))

    if args.format == "json":
        print(json.dumps(repos, indent=2, ensure_ascii=False))
    elif args.format == "csv":
        writer = csv.writer(sys.stdout)
        writer.writerow(["name", "private", "description", "html_url", "updated_at"])
        for r in repos:
            writer.writerow([r.get("name"), r.get("private"), r.get("description") or "", r.get("html_url"), r.get("updated_at")])
    else:
        print(format_markdown(repos))

if __name__ == "__main__":
    main()