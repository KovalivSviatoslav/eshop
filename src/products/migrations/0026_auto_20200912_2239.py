# Generated by Django 3.1 on 2020-09-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20200912_2157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категорію', 'verbose_name_plural': 'категорії'},
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='датою добавлення'),
        ),
    ]