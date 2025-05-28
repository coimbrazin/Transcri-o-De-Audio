import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configura a API do Gemini com a sua chave personalizada
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Modelo Gemini
model = genai.GenerativeModel('gemini-2.0-flash')

def detectar_idioma(texto):
    prompt = f"""Detecte se o texto abaixo está em português ou inglês. 
Responda apenas com uma das palavras: "português" ou "inglês". 
Nada mais.

Texto:
{texto}
"""
    resposta = model.generate_content(prompt)
    return resposta.text.strip().lower()

def traduzir(texto):
    idioma = detectar_idioma(texto)

    if idioma == "português":
        prompt = f"Traduza o texto abaixo para o inglês. Apenas a tradução, sem explicações:\n\n{texto}"
    elif idioma == "inglês":
        prompt = f"Traduza o texto abaixo para o português. Apenas a tradução, sem explicações:\n\n{texto}"
    else:
        return "❌ Não foi possível detectar o idioma do texto."

    resposta = model.generate_content(prompt)
    return resposta.text.strip()
