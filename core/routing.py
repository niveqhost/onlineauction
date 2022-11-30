from django.urls import path
from auction import consumers

websocket_urlpatterns = [
    path('ws/sc', consumers.MySyncConsumer.as_asgi()),
    path('ws/as', consumers.MyAsyncConsumer.as_asgi()),
]