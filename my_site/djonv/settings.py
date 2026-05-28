"""
Configuración global del proyecto Django 'djonv'.
Define las apps conectadas, seguridad, bases de datos, plantillas y archivos multimedia.
"""

from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta para la seguridad de la app
SECRET_KEY = 'django-insecure--ep20d864(wnbf@nw@h@$h7-kx0awuvxh2-sd7(-)mw3nnp-hu'

# Modo desarrollo activo (Muestra errores detallados)
DEBUG = True

# Hosts permitidos para acceder a la aplicación
ALLOWED_HOSTS = ['*']


# Definición de aplicaciones instaladas
INSTALLED_APPS = [
    'blog', # Tu aplicación del blog
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Capas intermedias de seguridad y procesamiento de peticiones
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Archivo de enrutamiento principal
ROOT_URLCONF = 'djonv.urls'

# Configuración del motor de plantillas HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Directorio global de plantillas
        'APP_DIRS': True, # Busca plantillas dentro de cada app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Punto de entrada para el servidor web síncrono
WSGI_APPLICATION = 'djonv.wsgi.application'


# Configuración de la Base de Datos (SQLite3)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validadores de contraseñas para el sistema de usuarios
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internacionalización e idioma
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Control de archivos estáticos (CSS, JS, Imágenes de diseño)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "blog" / 'static'
]

# Control de archivos multimedia (Imágenes subidas por usuarios)
MEDIA_URL = '/media/' # URL de acceso en el navegador
MEDIA_ROOT = BASE_DIR / 'media' # Ruta física en el disco duro