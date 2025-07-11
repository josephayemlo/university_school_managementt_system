from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/groupchat/<int:room_id>/', consumers.GroupChatConsumer.as_asgi()),
    path('ws/privatechat/<int:user_id>/', consumers.PrivateChatConsumer.as_asgi()),
]

