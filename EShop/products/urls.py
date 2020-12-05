from django.urls import path
from .views import products_list, product_detail, products_category

urlpatterns = [
    path('products/', products_list, name='products_list_url'),
    path('product/<str:slug>/', product_detail, name='product_detail_url'),
    path('category/<str:slug>/', products_category, name='products_category_url')
]