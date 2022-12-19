from django.urls import path
from auction import consumers

websocket_urlpatterns = [
    path('ws/auction/<int:product_id>/<slug:product_slug>', consumers.MySyncConsumer.as_asgi()),
]