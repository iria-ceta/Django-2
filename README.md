# Proyecto de Django

## Introducción
Este es un proyecto en el que he usado el framework Django para crear una web de blogs sobre programación. La idea es que sea un sitio donde cualquiera pueda entrar a echar un vistazo a noticias del sector o seguir algunos tutoriales prácticos.

## Instal·lación ràpida
1. Inicie una terminal y ejecute el siguiente comando para clonar el repositorio del proyecto:
   `git clone https://github.com/iria-ceta/Django-2.git`
2. Navegue al directorio principal del proyecto utilizando el comando:
   `cd my_site`
4. Es recomendable crear un entorno virtual para gestionar las dependencias del proyecto de forma aislada. Utilice el siguiente comando:
   `python -m venv env_site`
5. Active el entorno virtual recién creado con la siguiente instrucción:
   `.\env_site\Scripts\activate.ps1`
6. Instale las librerías necesarias para el proyecto, incluyendo Django, mediante el comando:
   `python -m pip install django`
7. Antes de iniciar el servidor, es fundamental aplicar las migraciones para configurar la base de datos. Ejecute los siguientes comandos en secuencia:
   `python  manage.py makemigrations` 
   `python manage.py migrate`

## Execución del proyecto
1. Active el servidor de desarrollo de Django con el comando:
   `python manage.py runserver` 
3. La aplicación estará accesible a través de su navegador web en la siguiente dirección:
   `http://127.0.0.1:8000`

## Pydocs
1. Views.py: https://iria-ceta.github.io/Django-2/blog.views.html
2. Models.py: https://iria-ceta.github.io/Django-2/blog.models.html
