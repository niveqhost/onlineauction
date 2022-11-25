from django.urls import path
from authentication import views

app_name = 'authentication'
urlpatterns = [
    path("register/", views.RegisterUser.as_view() , name="register"),
    path("login/", views.LoginUser.as_view() , name="login"),
    path('activate/<uidb64>/<token>', views.ActivateUser.as_view(), name='activate'),
]