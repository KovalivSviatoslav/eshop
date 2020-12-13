from django.db import models
from phonenumber_field import modelfields
from products.models import Product


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=60, db_index=True, null=True, verbose_name="ім'я")
    last_name = models.CharField(max_length=60, db_index=True, null=True, verbose_name="прізвище")
    phone = modelfields.PhoneNumberField(db_index=True, null=True, blank=False, verbose_name='номер телефону')
    email = models.EmailField(max_length=60, db_index=True, blank=True, null=True, verbose_name='емейл')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='датою заповнення')
    update_at = models.DateTimeField(auto_now=True, verbose_name='дата оновлення')

    def __str__(self):
        return f'{self.phone}({self.first_name})'

    class Meta:
        verbose_name = 'клієнт'
        verbose_name_plural = 'клієнти'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='клієнт')
    delivery_city = models.CharField(max_length=30, null=True, verbose_name='місто')
    np_warehouses = models.CharField(max_length=100, null=True, verbose_name='адрес відділення')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='загальна вартість замовлення')
    STATUS_CHOICES = [
        ('NW', 'Новий'),
        ('PC', 'Комплектується'),
        ('TD', 'Переданий на доставку'),
        ('CP', 'Виконаний'),
        ('CN', 'Скасований'),
        ('RT', 'Повернення')
    ]
    order_status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='NW', verbose_name='Статус')
    comment = models.TextField(max_length=240, blank=True, verbose_name='коментар')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='датою заповнення')
    update_at = models.DateTimeField(auto_now=True, verbose_name='дата оновлення')

    def __str__(self):
        return f'{self.customer.id} - {self.customer.phone}({self.customer.first_name})'

    class Meta:
        verbose_name = 'замовлення'
        verbose_name_plural = 'замовлення'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='замовлення')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='товар')
    quantity = models.PositiveIntegerField(default=1, null=False, blank=False, verbose_name='кількість')
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='ціна за шт.')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='ціна')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'товар в замовленні'
        verbose_name_plural = 'товари в замовленні'

    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price
        self.total_price = self.price_per_item * self.quantity
        super().save(*args, **kwargs)

        all_product_in_order = ProductInOrder.objects.filter(order=self.order)
        total_price = 0
        for order in all_product_in_order:
            total_price += order.total_price
        self.order.total_price = total_price
        self.order.save()