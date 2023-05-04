#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context
# Comando a usar para version especifica de python:  /opt/homebrew/bin/python3.10 -m pip install

import whisper
import random, string, os
import mongodb as mongo_access
import texttovoice as text_to_voice
from flask import Flask, jsonify, request, Response
from flask_sslify import SSLify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)   # Crea una instancia de la aplicación Flask
sslify = SSLify(app)    # Agrega redirección HTTPS a la aplicación Flask
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    return mongo_access.verify_user(username, password)


def generar_nombre_archivo():
    # Genera una cadena de caracteres aleatoria de longitud 10
    caracteres = string.ascii_letters + string.digits
    nombre_aleatorio = ''.join(random.choice(caracteres) for i in range(10))

    return nombre_aleatorio

def transcribe_a_texto(bytes, format):
    if not os.path.exists('archivos'):
        os.makedirs('archivos')
    
    nombre_archivo = generar_nombre_archivo();      # Obtiene el nombre que se le asigna al archivo.
    ruta_archivo = os.path.join('archivos', f"{nombre_archivo}.{format}")
    # Guarda el archivo en el directorio "archivos"
    with open(ruta_archivo, 'wb') as f:
        f.write(bytes)
    
    model = whisper.load_model("large")             # Carga el modelo de transcripción
    result = model.transcribe(ruta_archivo)         # Transcribe el archivo MP3

    if os.path.exists(ruta_archivo):
        os.remove(ruta_archivo)
    return jsonify({'texto': result["text"], 'lenguaje': result["language"]})         # Devuelve el texto de la transcripción como JSON

# Define la ruta '/transcribe' para recibir archivos MP3 y devolver texto
@app.route('/transcribe', methods=['POST'])
@auth.login_required
def get_text_file():
    archivo = request.files['archivo']              # Obtiene el archivo Audio o Video desde la solicitud
    formato = request.form['formato']               # Obtiene el formato desde la solicitud

    return transcribe_a_texto(archivo.read(), formato)

# Define la ruta '/transcribeByte' para recibir bytes de un archivo MP3 y devolver texto
@app.route('/transcribeByte', methods=['POST'])
@auth.login_required
def get_text_byte():
    bytes_archivo = request.data                    # Obtiene el arreglo de bytes desde la solicitud
    formato = request.form['formato']               # Obtiene el formato desde la solicitud

    return transcribe_a_texto(bytes_archivo, formato)

# Define la ruta '/textToVoice' recibe texto y envía audio.
@app.route('/textToVoice', methods=['POST'])
@auth.login_required
def texto_to_voice():
    texto = request.form['texto']
    bytes_audio = text_to_voice.convert_audio(texto)
    return Response(bytes_audio, mimetype="audio/mp3")


if __name__ == '__main__':  # host='0.0.0.0', port=5000
    app.run(debug=True)  # Inicia la aplicación en modo debug (solo para desarrollo[Debug=True])
