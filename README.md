# Whisper

Proyecto creado para que funcione como una API.

## Actualmente tiene 3 métodos:
  
  1. Transcribe (POST): *** Convierte el archivo haciendo la transcripción a texto ***
    > En cuál recibe 2 parámetros:
      - **archivo**: se obtiene el audio o video desde la solicitud.
      - **formato**: se indica el formato del archivo. Ejemplo: mp3 o mp4.
  2. TranscribeByte (POST): *** Convierte el archivo haciendo la transcripción a texto ***
    > En el cuál recibe 2 parámetros:
      - **bytes**: Se obtiene del header los bytes del archivo.
      - **formato**: se obtiene del body el formato del archivo.
  3. TextToVoice (POST): *** Texto pasa audio. ***
    > En el cuál recibe 1 solo parámetro:
      - **texto**: Desde el body el texto a convertir a audio.
