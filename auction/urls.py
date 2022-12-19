from django.urls import path

from auction import views

app_name = 'auction'
urlpatterns = [
    path('', views.IndexView.as_view() , name='index'),
    path('seller/sell-product', views.AddProduct.as_view() , name='add_product'),
    path('product', views.ProductView.as_view(), name='product'),
    path('product/<int:product_id>/<slug:product_slug>', views.ProductDetail.as_view(), name='product_detail'),
    path('category/<slug:category_slug>', views.CategoryDetail.as_view(), name='category_detail'),
]