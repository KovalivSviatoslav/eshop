# Generated by Django 3.1 on 2020-08-23 09:20

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20200823_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(null=True, upload_to='product_image_uploader', verbose_name='посилання'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(null=True, upload_to=products.models.product_main_image_uploader, verbose_name='посилання'),
        ),
    ]
