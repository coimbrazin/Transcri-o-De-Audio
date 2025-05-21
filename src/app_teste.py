import streamlit as st
from transcriber import transcrever_audio
from pathlib import Path
import time

# Imagem de fundo cobrindo tudo
def set_background(url):
    st.markdown(
        f"""
        <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {{
            margin: 0;
            padding: 0;
            height: 100%;
            background: url("{url}") no-repeat center center fixed;
            background-size: cover;
        }}

        [data-testid="stHeader"] {{
            background: transparent;
        }}

        [data-testid="stToolbar"] {{
            display: none;
        }}

        .block-container {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 1rem;
            margin-top: 0 !important;
        }}

        /* Gradient custom progress bar */
        .stProgress > div > div > div > div {{
            background: linear-gradient(to right, #00c6ff, #0072ff);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Nova imagem de fundo
set_background("https://images3.alphacoders.com/132/thumb-1920-1323165.png")

# Título
st.title("Transcrição de Áudio com IA 🎧")

# Upload do áudio
audio = st.file_uploader("Envie um arquivo de áudio", type=["mp3", "wav", "ogg"])

# Verificação e transcrição
if audio is not None:
    caminho = Path("audios") / audio.name
    caminho.parent.mkdir(exist_ok=True)
    with open(caminho, "wb") as f:
        f.write(audio.read())

    st.audio(caminho)

    # Barra de progresso com efeito visual
    st.subheader("🔄 Transcrevendo seu áudio:")
    progress_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.01)  # Simula tempo de carregamento
        progress_bar.progress(percent_complete + 1)

    texto = transcrever_audio(caminho)

    st.subheader("📝 Transcrição:")
    st.write(texto)
