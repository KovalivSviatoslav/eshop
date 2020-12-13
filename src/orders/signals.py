from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import ProductInOrder

@receiver(post_delete, sender=ProductInOrder)
def post_delete_order_total_price(sender, instance, **kwargs):
    all_products_in_order = ProductInOrder.objects.filter(order=instance.order)

    if all_products_in_order:
        total_price = 0
        for products in all_products_in_order:
            total_price += products.total_price
        products.total_price = total_price
        products.save()
