import os
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from io import BytesIO

# create directory if it doesn't exist
os.makedirs("Audios", exist_ok=True)
# download and load all models
preload_models()

def convert_audio(text, name):
     # generate audio from text
     text_prompt = "" + text + ""
     audio_array = generate_audio(text_prompt)
     # convert audio to MP3 format
     filename = os.path.join("Audios", name)
     # save audio to disk
     write_wav(filename, SAMPLE_RATE, audio_array)
     return filename

def convert_audio(text):
     # generate audio from text
     text_prompt = "" + text + ""
     audio_array = generate_audio(text_prompt, history_prompt="v2/es_speaker_0")
     # escribir los bytes del archivo de audio en un objeto BytesIO
     audio_bytes_io = BytesIO()
     write_wav(audio_bytes_io, SAMPLE_RATE, audio_array)
     # devolver los bytes del archivo de audio
     return audio_bytes_io.getvalue()