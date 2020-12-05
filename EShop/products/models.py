import json
from django.db import models
from django.shortcuts import reverse
from mptt.models import MPTTModel, TreeForeignKey


# Image-nav
def product_main_image_uploader(instance, filename):
    return f'static/products/images/{instance.manufacturer.name}/{instance.id}/{filename}'


def product_slide_uploader(instance, filename):
    return f'static/products/images/{instance.product.manufacturer.name}/{instance.product.id}/{filename}'


# Create your models here.
class Product(models.Model):
    """Товар"""
    name = models.CharField(max_length=60, null=True, db_index=True, verbose_name='назва')
    slug = models.SlugField(max_length=60, unique=True)
    main_image = models.ImageField(upload_to=product_main_image_uploader, verbose_name='основне фото', blank=False, null=True)
    description = models.TextField(blank=True, db_index=True, verbose_name='опис')
    manufacturer = models.ForeignKey(
        'ProductManufacturer', on_delete=models.SET_NULL, null=True, db_index=True, related_name='products', verbose_name='виробник'
    )
    categories = models.ManyToManyField('Category', blank=True, related_name='products', verbose_name='категорія')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='ціна')
    stock = models.PositiveIntegerField(null=True, verbose_name='на складі')
    is_active = models.BooleanField(default=False, verbose_name='продається')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='датою добавлення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата оновлення')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товари'

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    @property
    def main_imageURL(self):
        try:
            url = self.main_image.url
        except:
            url = '/static/main/png/NO_IMG.png'
        return url

    def get_json_data(self):
        data = {
            'id': str(self.id),
            'name': self.name,
            'image': str(self.main_imageURL),
            'price': str(self.price),
        }
        json_data = json.dumps(data, ensure_ascii=False)
        return json_data


class ProductSlide(models.Model):
    """Фото товару"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery', verbose_name='товар')
    slide = models.ImageField(upload_to=product_slide_uploader, verbose_name='посилання', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавлення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата оновлення')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'слайд'
        verbose_name_plural = 'слайди'
        ordering = ['created_at']

    @property
    def slideURL(self):
        try:
            url = self.slide.url
        except:
            url = '/static/main/png/NO_IMG.png'
        return url


class ProductManufacturer(models.Model):
    """Виробник"""
    name = models.CharField(max_length=60, unique=True, verbose_name='назва')
    description = models.TextField(blank=True, verbose_name='опис')
    logo = models.ImageField(
        upload_to='static/products/images/manufacturer_logo/', verbose_name='завантажити', blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'виробник'
        verbose_name_plural = 'виробники'

    @property
    def logoURL(self):
        try:
            url = self.logo.url
        except:
            url = '/static/main/png/NO_IMG.png'
        return url


class Category(MPTTModel):
    """Категорія"""
    name = models.CharField(max_length=60, db_index=True, verbose_name='назва')
    short_desc = models.TextField(max_length=160, blank=True, verbose_name='короткий опис')
    slug = models.SlugField(max_length=40, unique=True)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Основна категорія'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категорію'
        verbose_name_plural = 'категорії'

    class MPTTMeta:
        order_insertion_by = ['name']

    def get_absolute_url(self):
        return reverse('products_category_url', kwargs={'slug': self.slug})
