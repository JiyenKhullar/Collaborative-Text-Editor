"""
ASGI config for collab_text_editor project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from editor import consumers  # We will create this next

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collab_text_editor.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/document/<int:document_id>/', consumers.DocumentConsumer.as_asgi()),  # WebSocket endpoint
        ])
    ),
})

