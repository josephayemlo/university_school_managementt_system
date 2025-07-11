import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import ChatRoom, GroupMessage, PrivateMessage

User = get_user_model()

class GroupChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f"groupchat_{self.room_id}"
        self.user = self.scope["user"]

        # Join group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message", "")

        # Save to DB
        await self.save_message(self.room_id, self.user, message)

        # Broadcast message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": self.user.first_name,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "sender": event["sender"],
        }))

    @database_sync_to_async
    def save_message(self, room_id, user, message):
        room = ChatRoom.objects.get(id=room_id)
        return GroupMessage.objects.create(room=room, sender=user, body=message)


# private message
class PrivateChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.other_user_id = int(self.scope["url_route"]["kwargs"]["user_id"])

        # Prevent chatting with yourself
        if self.user.id == self.other_user_id:
            print(f"[DENY] ❌ User {self.user.id} tried to chat with self.")
            self.connected = False  # ❗ Mark as not connected to group
            await self.close()
            return

        self.room_name = self.get_room_name(self.user.id, self.other_user_id)
        self.room_group_name = f"privchat_{self.room_name}"
        self.connected = True  # ✅ Mark as connected

        print(f"[CONNECT] ✅ User {self.user.id} joined group: {self.room_group_name}")

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        if getattr(self, "connected", False):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )


    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message", "")

        await self.save_private_message(self.user.id, int(self.other_user_id), message)
      # ✅ LOG 2: Message sent
        print(f"[SEND] User {self.user.id} sent message to group: {self.room_group_name} => {message}")

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": self.user.first_name,
            }
        )

    async def chat_message(self, event):
         # ✅ LOG 3: User received message
        print(f"[RECEIVE] User {self.user.id} received message in group {self.room_group_name}: {event['message']}")

        await self.send(text_data=json.dumps({
            "message": event["message"],
            "sender": event["sender"],
        }))

    @database_sync_to_async
    def save_private_message(self, sender_id, receiver_id, message):
        sender = User.objects.get(id=sender_id)
        receiver = User.objects.get(id=receiver_id)
        return PrivateMessage.objects.create(sender=sender, receiver=receiver, body=message)

# virtual room for private users
    def get_room_name(self, user1_id, user2_id):
        # Always sort to ensure both users connect to same group
        return f"{min(user1_id, user2_id)}_{max(user1_id, user2_id)}"
