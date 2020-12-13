from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from mptt.admin import DraggableMPTTAdmin
from mptt.admin import TreeRelatedFieldListFilter

from .models import Product, ProductSlide, ProductManufacturer, Category


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    fields = ('parent', 'name', 'slug', 'short_desc')
    list_display = ('tree_actions', 'indented_title')
    prepopulated_fields = {'slug': ('name',)}
    mptt_level_indent = 20


# @admin.register(ProductSlide)
# class ProductSlideAdmin(admin.ModelAdmin):
#     pass


class ProductSlideInline(admin.TabularInline):
    """Меню Фотографій, зв'язаних з обраним товаром в адмінці."""
    model = ProductSlide
    extra = 0
    max_num = 6
    readonly_fields = ('admin_product_image',)

    def admin_product_image(self, instanse):
        """Надає можливість відобразити всі фотографії обраного товару в адмінці."""
        return mark_safe(f'<img src="{instanse.slideURL}" width="150" />')

    admin_product_image.short_description = 'логотип'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Меню Товару в адмінці."""
    fields = ('id', ('name', 'slug'), 'admin_product_photo', 'main_image', 'description', 'manufacturer', 'categories', 'price', ('stock', 'is_active'))
    readonly_fields = ('admin_product_photo', 'id')
    list_display = ('id', 'name', 'admin_product_photo', 'description', 'manufacturer', 'stock', 'price', 'is_active')
    list_display_links = ('name', 'admin_product_photo')
    list_filter = ('created_at', ('categories', TreeRelatedFieldListFilter), 'manufacturer', 'is_active')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name', 'description', 'manufacturer__name']
    inlines = [
        ProductSlideInline,
    ]
    view_on_site = True
    filter_horizontal = ('categories',)

    def save_model(self, request, obj, form, change):
        if obj.stock <= 0:
            obj.is_active = False
        obj.save()

    def admin_product_photo(self, instanse):
        """Надає можливість відобразити 'основне' фото обраного товару адмінці."""
        return mark_safe(f'<img src="{instanse.main_imageURL}" width="110"/>')

    admin_product_photo.short_description = 'основне фото'


@admin.register(ProductManufacturer)
class ProductManufacturerAdmin(admin.ModelAdmin):
    """Меню Виробника в адмінці."""
    list_display = ('name', 'description', 'admin_manufacture_logo')
    readonly_fields = ('admin_manufacture_logo',)

    def admin_manufacture_logo(self, instanse):
        """Надає можливість відобразити логотип виробника в адмінці."""
        return mark_safe(f'<img src="{instanse.logoURL}" width="250" />')

    admin_manufacture_logo.short_description = 'логотип'
