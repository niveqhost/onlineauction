from django.urls import path, include

websocket_urlpatterns = [
    path("ws/sc", include("django.conf.urls.i18n")),
]