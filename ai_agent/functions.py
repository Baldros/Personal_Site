# Exclusivo para envio de Email via SMTP
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import streamlit as st

# ==================================================================
# Funções de Análise de Contexto:
# ==================================================================

import pandas as pd

def load_dataframe(file_path):
    """Load a dataframe from a CSV or Excel file."""
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")

def list_categories(dataframe, column_name):
    """List all unique categories in a column of a dataframe."""
    if column_name not in dataframe.columns:
        return f"Error: Column '{column_name}' not found. Available columns: {list(dataframe.columns)}"
    return dataframe[column_name].unique().tolist()

def get_element(dataframe, category, column_name_search, column_name_target):
    """Get content from a target column where search column matches category."""
    try:
        if column_name_search not in dataframe.columns or column_name_target not in dataframe.columns:
             return f"Error: Columns invalid. Available: {list(dataframe.columns)}"
             
        result = dataframe[dataframe[column_name_search] == category][column_name_target].values
        if len(result) > 0:
            return result[0]
        return "No match found."
    except Exception as e:
        return f"Error extracting element: {e}"

def read_md_content(file_path):
    """Read the content of a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# ==================================================================
# Funções de Envio de Email:
# ==================================================================


def send_email_logic(
    assunto,
    corpo,
    destinatarios = st.secrets("EMAIL_USER"),
    remetente = st.secrets("EMAIL_SENDER"),
    senha = st.secrets("EMAIL_PASSWORD"),
    anexos=None,
    html=False
):
    """
    Envia email usando Gmail e SMTP.
    
    Args:
        remetente (str): Email do remetente (Gmail)
        senha (str): Senha de app do Gmail (não a senha normal)
        destinatarios (list ou str): Email(s) do(s) destinatário(s)
        assunto (str): Assunto do email
        corpo (str): Corpo do email
        anexos (list, optional): Lista de caminhos dos arquivos para anexar
        html (bool, optional): Se True, envia como HTML. Padrão é False (texto simples)
    
    Returns:
        bool: True se enviado com sucesso, False caso contrário
    """
    
    try:
        # Cria a mensagem
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['Subject'] = assunto
        
        # Configura destinatários
        if isinstance(destinatarios, str):
            destinatarios = [destinatarios]
        msg['To'] = ', '.join(destinatarios)
        
        # Adiciona o corpo do email
        tipo = 'html' if html else 'plain'
        msg.attach(MIMEText(corpo, tipo, 'utf-8'))
        
        # Adiciona anexos se houver
        if anexos:
            for arquivo in anexos:
                if os.path.exists(arquivo):
                    with open(arquivo, 'rb') as f:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(f.read())
                        encoders.encode_base64(part)
                        part.add_header(
                            'Content-Disposition',
                            f'attachment; filename={os.path.basename(arquivo)}'
                        )
                        msg.attach(part)
                else:
                    print(f"Aviso: Arquivo '{arquivo}' não encontrado")
        
        # Conecta ao servidor SMTP do Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Inicia criptografia TLS
        
        # Faz login
        server.login(remetente, senha)
        
        # Envia o email
        server.send_message(msg)
        
        # Fecha a conexão
        server.quit()
        
        return "Email enviado com sucesso! :)"
        
    except smtplib.SMTPAuthenticationError:
        return "Erro de autenticação. Verifique seu email e senha de app."

    except smtplib.SMTPException as e:
        return "Erro SMTP: {e}"
    
    except Exception as e:
        return "Erro ao enviar email: {e}"

# ==================================================================
# GitHub Functions
# ==================================================================

import requests
from typing import List, Dict

def get_baldros_repos() -> List[Dict]:
    """
    Busca todos os repositórios públicos do usuário Baldros.
    
    Returns:
        Lista de dicionários com informações dos repositórios
    """
    repos = []
    url = "https://api.github.com/users/Baldros/repos"
    
    while url:
        response = requests.get(url, params={"per_page": 100})
        response.raise_for_status()
        
        repos.extend(response.json())
        
        # Verifica se há próxima página
        link_header = response.headers.get("Link", "")
        url = None
        
        for part in link_header.split(","):
            if 'rel="next"' in part:
                url = part[part.find("<") + 1:part.find(">")]
                break
    
    return repos
