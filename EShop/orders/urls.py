from django.urls import path
from .views import order_checkout

urlpatterns = [
    # path('cart/', CartView.as_view(), name='order_cart_url'),
    path('checkout/', order_checkout, name='order_checkout_url'),
]
