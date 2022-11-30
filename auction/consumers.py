from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

#* Xu ly dong bo
class MySyncConsumer(WebsocketConsumer):
    # Lang nghe ket noi tu phia client
    def connect(self):
        # Dong y ket noi
        self.accept()
        # Tu choi ket noi
        # self.close()
        # Gui thong bao toi client
        self.send(text_data="Welcome to synchronous websocket server!")

    # Nhan tin nhan tu phia client gui den
    def receive(self, text_data=None):
        # Gui tin nhan ve lai phia client
        self.send(text_data="Hello client!")
        # Buoc ngat ket noi
        # self.close()
        # Dong ket noi voi ma code -> tao ra error code
        # self.close(code=4123)

    # Client hoac server ngat ket noi
    def disconnect(self, close_code):
        # Dong ket noi, close_code mac dinh la 1000
        self.close(close_code)

#* Xu ly bat dong bo
class MyAsyncConsumer(AsyncWebsocketConsumer):
    # Lang nghe ket noi tu phia client
    async def connect(self):
        # Dong y ket noi
        await self.accept()
        # Tu choi ket noi
        # await self.close()
        # Gui thong bao toi client
        await self.send(text_data="Welcome to asynchronous websocket server!")

    # Nhan tin nhan tu phia client gui den
    async def receive(self, text_data=None):
        # Gui tin nhan ve lai phia client
        await self.send(text_data="Hello client!")
        # Buoc ngat ket noi
        # await self.close()
        # Dong ket noi voi ma code -> tao ra error code
        # self.close(code=4123)

    # Client hoac server ngat ket noi
    async def disconnect(self, close_code):
        # Dong ket noi, close_code mac dinh la 1000
        await self.close(close_code)