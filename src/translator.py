import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configura a API do Gemini com a chave da variável de ambiente
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Inicializa o modelo
model = genai.GenerativeModel('gemini-2.0-flash')

def detectar_idioma(texto):
    prompt = f"""
Detecte se o texto abaixo está em português ou inglês. 
Responda apenas com uma das palavras: "português" ou "inglês". Nada mais.

Texto:
{texto}
"""
    try:
        resposta = model.generate_content(prompt)
        return resposta.text.strip().lower()
    except Exception as e:
        return "erro"

def traduzir(texto):
    idioma = detectar_idioma(texto)

    if idioma == "português":
        prompt = f"Traduza o texto abaixo para o inglês. Apenas a tradução, sem explicações:\n\n{texto}"
    elif idioma == "inglês":
        prompt = f"Traduza o texto abaixo para o português. Apenas a tradução, sem explicações:\n\n{texto}"
    elif idioma == "erro":
        return "❌ Erro ao detectar o idioma."
    else:
        return "❌ Idioma não identificado. Use apenas português ou inglês."

    try:
        resposta = model.generate_content(prompt)
        return resposta.text.strip()
    except Exception as e:
        return f"❌ Erro ao traduzir: {str(e)}"
