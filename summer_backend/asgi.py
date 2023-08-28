"""
ASGI config for summer_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'summer_backend.settings')
django.setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
import message.routing



application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(chat.routing.websocket_urlpatterns + message.routing.websocket_urlpatterns)
})
