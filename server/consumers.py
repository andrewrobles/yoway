import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Order, Food


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        name = text_data_json.get('name', None)
        instructions = text_data_json.get('instructions', '')
        selected_food_ids = text_data_json.get('selectedFoodIds', [])        
        if name:
            await sync_to_async(self.submit_order)(name, instructions, selected_food_ids)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'name': name,
                'instructions': instructions,
            }
        )
    
    def submit_order(self, name, instructions, selected_food_ids):
        print(f'selected_food_ids:{selected_food_ids}')
        order = Order.objects.create(
            name=name, 
            instructions=instructions
        )
        for id in selected_food_ids:
            food = Food.objects.get(id=id)
            order.food.add(food)

    # Receive message from room group
    async def chat_message(self, event):
        name = event.get('name', None)
        instructions = event.get('instructions', '')

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'name': name,
            'instructions': instructions
        }))