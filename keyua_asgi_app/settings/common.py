from os import getenv, path
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True if getenv('DEBUG', 'true') == 'true' else False

ROOT_URLCONF = 'keyua_asgi_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'keyua_asgi_app.wsgi.application'
ASGI_APPLICATION = 'keyua_asgi_app.asgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = path.join(BASE_DIR, 'staticroot')
STATICFILES_DIRS = [
    path.join(BASE_DIR, 'static'),
]