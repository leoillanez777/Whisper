# Manual de Instalaci�n - Voz a Texto

Este manual te guiar� en el proceso de instalaci�n de Voz a Texto, un programa que convierte voz a texto utilizando la API de OpenAI.


## Paso 1: Instalar Python


Primero, debes instalar Python en tu computadora. Aseg�rate de descargar e instalar la versi�n 3.10 de Python, ya que la API de voz a texto actualmente funciona con esa versi�n y no con la �ltima (3.11) al momento de la creaci�n de este manual.


## Paso 2: Instalar Git


Despu�s, debes instalar Git para poder instalar Whisper con el siguiente comando:

    pip install git+https://github.com/openai/whisper.git

Para m�s informaci�n sobre c�mo instalar Whisper, puedes acceder al siguiente enlace: https://github.com/openai/whisper.


## Paso 3: Instalar bibliotecas adicionales


En este paso, debes instalar las siguientes bibliotecas adicionales:

 - pymongo: para la conexi�n con la base de datos MongoDB.
 - bcrypt: para el cifrado de contrase�as.
 - flask: para el desarrollo de la aplicaci�n web.
 - flask_sslify: para redirigir todas las solicitudes a HTTPS.
 - flask_httpauth: para autenticar a los usuarios.

Puedes instalar estas bibliotecas con los siguientes comandos:

    pip install pymongo
    pip install bcrypt
    pip install flask
    pip install flask_sslify
    pip install flask_httpauth


## Paso 4: Configurar el servicio de Windows


Para ejecutar la aplicaci�n de Voz a Texto como un servicio de Windows, debes seguir los siguientes pasos:

 1. Abre la terminal y ub�cate en donde se encuentre el archivo
    "nssm.exe". En este caso, en "C:\VozaTexto\nssm-2.24\win64".
 2. Ejecuta la siguiente l�nea: `nssm install VozATexto`
 3. Completa los siguientes datos en la ventana que se abrir�: 
	 - **Path:** la
	        ubicaci�n del ejecutable de Python. (ejemplo en
	        "C:\Python\python.exe")
       
	 - **Startup Directory:** la ubicaci�n de la
	       carpeta del proyecto.
	       
	 - **Arguments:** el comando a ejecutar en este caso
	       "app.py"

4. Haz clic en el bot�n "Install service" para instalar el servicio.
5. Para iniciar el servicio, abre el "Administrador de servicios" de Windows, busca el servicio "VozATexto" y haz clic en "Iniciar".

**�Listo!** 
Ahora puedes utilizar Voz a Texto para convertir voz a texto de forma sencilla y r�pida.