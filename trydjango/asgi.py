import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
import public_chat.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trydjango.settings')


    # Just HTTP for now. (We can add other protocols later.)

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            public_chat.routing.websocket_urlpatterns
        )
    )
})