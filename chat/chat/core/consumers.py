import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import ChatRoom


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_code = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = f'chat_{self.room_code}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
        channels_amount = len(self.channel_layer.groups.get(self.room_group_name, {}))
        if channels_amount == 0:
            self.delete_room(self.room_code)
    
    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)

        message = data['message']
        username = data['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'message',
                'message': message,
                'username': username
            }
        )
    
    async def message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
    
    @sync_to_async
    def delete_room(self, room_code):
        chatroom = ChatRoom.objects.get(invite_code=self.room_code)
        chatroom.delete()
