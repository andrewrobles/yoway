import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Food, Order, FoodOrder


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
        food_orders = text_data_json.get('foodOrders', [])
        if name:
            await sync_to_async(self.submit_order)(
                name, 
                instructions, 
                food_orders
            )
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'name': name,
                'instructions': instructions,
                'foodOrders': food_orders
            }
        )
    
    def submit_order(self, name, instructions, food_orders):
        order = Order.objects.create(
            instructions=instructions,
            name=name, 
        )
        for food_order in food_orders:
            FoodOrder.objects.create(
                food = Food.objects.get(id=food_order['foodId']),
                quantity=food_order['foodQuantity'],
                order = order,
            )

    # Receive message from room group
    async def chat_message(self, event):
        name = event.get('name', None)
        instructions = event.get('instructions', '')
        food_orders = event.get('foodOrders', [])

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'name': name,
            'instructions': instructions,
            'foodOrders': food_orders
        }))