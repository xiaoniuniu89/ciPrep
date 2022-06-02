from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # return await super().connect()
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
    
       
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
            }
        )
        
    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))
        
   
    
    async def disconnect(self, close_code):
        # return await super().disconnect(code)
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


class CodeEditorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # return await super().connect()
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        value = text_data_json['value']
        eventDiv = text_data_json['eventDiv']
        line = text_data_json['line']
        ch = text_data_json['ch']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'editor_message',
                'value': value,
                'eventDiv': eventDiv,
                'line': line,
                'ch': ch
            }
        )
        
    async def editor_message(self, event):
        value = event['value']
        eventDiv = event['eventDiv']
        line = event['line']
        ch = event['ch']
        await self.send(text_data=json.dumps({
            'value': value,
            'eventDiv': eventDiv,
            'line': line,
            'ch': ch
        }))
    pass
    