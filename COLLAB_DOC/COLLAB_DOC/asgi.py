"""
ASGI config for COLLAB_DOC project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from Documentos.consumers import DocumentConsumer


from Documentos.routing import websocket_urlpatterns
import pika

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'COLLAB_DOC.settings')

django_asgi_app = get_asgi_application()
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
connection.channel().exchange_declare(exchange='documentos',
                    exchange_type='direct')
connection.close()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        # Just HTTP for now. (We can add other protocols later.)
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(websocket_urlpatterns)
            )
        ),
    }
)