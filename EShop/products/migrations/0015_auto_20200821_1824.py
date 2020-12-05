# Generated by Django 3.1 on 2020-08-21 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20200821_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='products.Product', verbose_name='товар'),
        ),
        migrations.AlterField(
            model_name='category',
            name='short_desc',
            field=models.TextField(blank=True, max_length=160, verbose_name='короткий опис'),
        ),
    ]