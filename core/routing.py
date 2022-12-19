from django.urls import path
from auction import consumers

websocket_urlpatterns = [
    path('ws/auction', consumers.MySyncConsumer.as_asgi()),
]