from django.urls import path

from auction import views

app_name = 'auction'
urlpatterns = [
    path('', views.IndexView.as_view() , name='index'),
    path('seller/sell-product', views.AddProduct.as_view() , name='add_product'),
    path('product', views.ProductView.as_view(), name='product'),
    path('product/<int:id>', views.ProductDetail.as_view(), name='product-detail'),
]