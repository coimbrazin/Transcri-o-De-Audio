import os
from pydub import AudioSegment
from pydub.utils import which
import whisper

# Configura o caminho do ffmpeg local (relativo ao arquivo atual)
ffmpeg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'libs', 'ffmpeg'))

# Adiciona o caminho do ffmpeg ao PATH do processo
os.environ["PATH"] += os.pathsep + ffmpeg_path

# Define explicitamente para o pydub quais executáveis usar
AudioSegment.converter = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")

def transcrever_audio(caminho_arquivo):
    # Carrega o áudio usando pydub
    audio = AudioSegment.from_file(caminho_arquivo)

    # Exporta para wav temporariamente (whisper recomenda wav)
    temp_wav = "temp.wav"
    audio.export(temp_wav, format="wav")

    # Carrega o modelo Whisper (pode ajustar o modelo para 'small', 'base', etc)
    modelo = whisper.load_model("base")

    # Faz a transcrição
    resultado = modelo.transcribe(temp_wav)

    # Remove o arquivo temporário (opcional)
    os.remove(temp_wav)

    return resultado['text']
