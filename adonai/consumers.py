# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # You can add logic here to handle different types of notifications
        message = json.loads(text_data)["message"]

        await self.send(text_data=json.dumps({
            "message": message
        }))
