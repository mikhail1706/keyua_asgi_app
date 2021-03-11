"""
ASGI config for keyua_asgi_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

import django

django.setup()

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import keyua_asgi_app.apps.cities.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'keyua_asgi_app.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            keyua_asgi_app.apps.cities.routing.websocket_urlpatterns
        )
    )
})
