import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import studentchat.routing  # Your app's routing file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # for regular HTTP views
    "websocket": AuthMiddlewareStack(
        URLRouter(
            studentchat.routing.websocket_urlpatterns  # points to your chat system
        )
    ),
})
