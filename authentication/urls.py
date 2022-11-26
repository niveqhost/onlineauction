from django.urls import path
from authentication import views

app_name = 'authentication'
urlpatterns = [
    path("register/", views.RegisterUser.as_view() , name="register"),
    path('activate/<uidb64>/<token>', views.ActivateUser.as_view(), name='activate'),
    path("login/", views.LoginUser.as_view() , name="login"),
    path("logout/", views.LogoutUser.as_view() , name="logout"),
    path("profile/", views.ViewProfile.as_view() , name="profile"),
    # path("profile/<user_id>", views.ViewProfile.as_view() , name="profile"),
]