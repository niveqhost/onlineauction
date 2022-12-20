import json
from datetime import timedelta
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from auction.models import *
from authentication.models import *
from utils import constants

#* Xu ly dong bo
class MySyncConsumer(WebsocketConsumer):
    
    # Lang nghe ket noi tu phia client
    def connect(self):
        self.user = self.scope['user']
        self.product_id = self.scope['url_route']['kwargs']['product_id']
        self.room_group_name = 'auction_%s' % self.product_id
        # Tham gia vao phong chat
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        # Dong y ket noi
        self.accept()
        # Gui thong bao toi client
        self.send_message('Welcome to synchronous websocket server!')

    # Nhan tin nhan tu phia client gui den
    def receive(self, text_data=None):
        data = json.loads(text_data)
        print('message received from client: ', data)
        if data['command'] in self.commands:
            self.commands[data['command']](self,data)

    # Client hoac server ngat ket noi
    def disconnect(self, close_code):
        # Xoa nhom chat
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        # Dong ket noi, close_code mac dinh la 1000
        self.close(close_code)

#* Custom function
    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Gui tin nhan toi toan bo thanh vien trong nhom
    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
        {
            # Dinh nghia ham chat_message de xu ly su kien
            'type': 'chat_message', 
            'message': message,
        })
        
    # Nhan tin nhan tu nhom WebSocket
    def chat_message(self, event):
        message = event['message']
        # Gui tin nhan toi WebSocket
        self.send(text_data=json.dumps(message))

    def fetch_messages(self, data):
        auction = AuctionLot.objects.get(id=int(data['auction_id']))
        histories = AuctionHistory.objects.filter(auction=auction)
        highest_price = AuctionHistory.objects.filter(auction=auction).order_by('-price').first()
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(histories),
            'highest_price' : highest_price.price
        }
        # Gui tin nhan den phia client
        return self.send_chat_message(content)

    # Xu li su kien khach hang dau gia
    def new_message(self, data):
        # Nguoi dau gia
        bidder = data['from']
        bid_user = CustomUser.objects.filter(username=bidder)[0]
        # Phien dau gia
        auction_id = int(data['auction_id'])
        auction = AuctionLot.objects.get(id=auction_id)
        # Tao lich su phien dau gia
        auction_history = AuctionHistory.objects.create(bidder=bid_user, price=data['message'], auction=auction)
        # Luu vao co so du lieu
        auction_history.save()
        content = {
            #'id':message.author.id,
            'command': 'new_message',
            'message': self.message_to_json(auction_history),
            'history_count': AuctionHistory.objects.filter(auction=auction).count()
        }
        return self.send_chat_message(content)


    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,
    }

    def message_to_json(self, message):
        return {
            'avatar': message.bidder.avatar.url,
            'bidder': message.bidder.username,
            'price': message.price,
            'date_bidded': str((message.date_bidded + timedelta(hours=constants.TIME_DIFFERENT)).strftime('%d/%m/%Y')),
            'time_bidded': str((message.date_bidded + timedelta(hours=constants.TIME_DIFFERENT)).strftime('%H:%M:%S')),
        }

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result