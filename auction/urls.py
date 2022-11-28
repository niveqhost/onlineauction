from django.urls import path, include
from auction import views

app_name = 'auction'
urlpatterns = [
    path('', views.IndexView.as_view() , name='index'),
    path('seller/', views.AddProduct.as_view() , name='add_product'),
]