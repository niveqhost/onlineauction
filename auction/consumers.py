from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

import json

#* Xu ly dong bo
class MySyncConsumer(WebsocketConsumer):
    # Lang nghe ket noi tu phia client
    def connect(self):
        self.user = self.scope['user']
        self.product_id = self.scope['url_route']['kwargs']['product_id']
        self.room_group_name = 'auction_%s' % self.product_id
        # join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print('Channel Layer: ', self.channel_layer)
        # Dong y ket noi
        self.accept()
        # Gui thong bao toi client
        self.send_message('Welcome to synchronous websocket server!')

    # Nhan tin nhan tu phia client gui den
    def receive(self, text_data=None):
        print('message received from client: ', text_data);
        # Gui tin nhan ve lai phia client
        self.send(text_data=json.dumps('Hello client 1!'))
        # Buoc ngat ket noi
        # self.close()
        # Dong ket noi voi ma code -> tao ra error code
        # self.close(code=4123)

    # Client hoac server ngat ket noi
    def disconnect(self, close_code):
        # Dong ket noi, close_code mac dinh la 1000
        self.close(close_code)

    # Custom
    def send_message(self, message):
        self.send(text_data=json.dumps(message))
    def send_chat_message(self, message):
        # Send message to WebSocket
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
        self.room_group_name,
        {
            'type': 'chat_message',
            'message': message,
        })