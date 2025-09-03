from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from .models import Message, Room


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = f"chat_{self.room_id}"
        user = self.scope["user"]
        if user.is_anonymous:
            await self.close()
            return
        try:
            room = await sync_to_async(Room.objects.get)(pk=self.room_id)
        except Room.DoesNotExist:
            await self.close()
            return
        is_participant = await sync_to_async(room.participants.filter(pk=user.pk).exists)()
        if not is_participant:
            await self.close()
            return
        self.room = room
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive_json(self, content, **kwargs):
        user = self.scope["user"]
        message_text = content.get("content")
        if not message_text:
            return
        message = await sync_to_async(Message.objects.create)(
            room=self.room, author=user, content=message_text
        )
        data = {
            "id": message.id,
            "author": user.id,
            "content": message.content,
            "created_at": message.created_at.isoformat(),
        }
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": data}
        )

    async def chat_message(self, event):
        await self.send_json(event["message"])
