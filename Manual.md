# Manual de Instalación - Voz a Texto

Este manual te guiará en el proceso de instalación de Voz a Texto, un programa que convierte voz a texto utilizando la API de OpenAI.


## Paso 1: Instalar Python


Primero, debes instalar Python en tu computadora. Asegúrate de descargar e instalar la versión 3.10 de Python, ya que la API de voz a texto actualmente funciona con esa versión y no con la última (3.11) al momento de la creación de este manual.


## Paso 2: Instalar Git


Después, debes instalar Git para poder instalar Whisper con el siguiente comando:

    pip install git+https://github.com/openai/whisper.git

Para más información sobre cómo instalar Whisper, puedes acceder al siguiente enlace: https://github.com/openai/whisper.


## Paso 3: Instalar bibliotecas adicionales


En este paso, debes instalar las siguientes bibliotecas adicionales:

 - pymongo: para la conexión con la base de datos MongoDB.
 - bcrypt: para el cifrado de contraseñas.
 - flask: para el desarrollo de la aplicación web.
 - flask_sslify: para redirigir todas las solicitudes a HTTPS.
 - flask_httpauth: para autenticar a los usuarios.

Puedes instalar estas bibliotecas con los siguientes comandos:

    pip install pymongo
    pip install bcrypt
    pip install flask
    pip install flask_sslify
    pip install flask_httpauth


## Paso 4: Configurar el servicio de Windows


Para ejecutar la aplicación de Voz a Texto como un servicio de Windows, debes seguir los siguientes pasos:

 1. Abre la terminal y ubícate en donde se encuentre el archivo
    "nssm.exe". En este caso, en "C:\VozaTexto\nssm-2.24\win64".
 2. Ejecuta la siguiente línea: `nssm install VozATexto`
 3. Completa los siguientes datos en la ventana que se abrirá: 
	 - **Path:** la
	        ubicación del ejecutable de Python. (ejemplo en
	        "C:\Python\python.exe")
       
	 - **Startup Directory:** la ubicación de la
	       carpeta del proyecto.
	       
	 - **Arguments:** el comando a ejecutar en este caso
	       "app.py"

4. Haz clic en el botón "Install service" para instalar el servicio.
5. Para iniciar el servicio, abre el "Administrador de servicios" de Windows, busca el servicio "VozATexto" y haz clic en "Iniciar".

**¡Listo!** 
Ahora puedes utilizar Voz a Texto para convertir voz a texto de forma sencilla y rápida.