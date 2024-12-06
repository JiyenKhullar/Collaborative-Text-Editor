import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DocumentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.document_id = self.scope['url_route']['kwargs']['document_id']
        self.room_group_name = f'document_{self.document_id}'

        # Join the document group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the document group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        content = data['content']

        # Send message to WebSocket group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'document_update',
                'content': content
            }
        )

    async def document_update(self, event):
        content = event['content']

        # Send document content update to WebSocket
        await self.send(text_data=json.dumps({
            'content': content
        }))
