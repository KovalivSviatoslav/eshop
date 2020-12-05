from django.contrib import admin
from .models import Customer, Order, ProductInOrder
# Register your models here.

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Меню Клієнта в адмінці"""
    list_display = ('first_name', 'last_name', 'phone', 'email')
    search_fields = ['first_name', 'last_name', 'phone', 'email']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Меню Замовлення в адмінці"""
    fields = ('customer', ('delivery_city', 'np_warehouses'), 'total_price', 'order_status', 'comment')
    list_display = ('id', 'customer', 'order_status', 'total_price', 'create_at', 'update_at')
    list_filter = ('create_at', 'order_status')
    inlines = [
        ProductInOrderInline
    ]