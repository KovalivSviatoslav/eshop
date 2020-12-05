# Generated by Django 3.1 on 2020-09-12 19:39

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200912_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='датою заповнення'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, null=True, region=None, verbose_name='номер телефону'),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='датою заповнення'),
        ),
    ]
