from django.urls import path
from authentication import views

app_name = 'authentication'
urlpatterns = [
    path("register/", views.UserRegister.as_view() , name="register"),
]