# Generated by Django 3.0.8 on 2020-08-08 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200802_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ['created_at'], 'verbose_name': 'фотографія', 'verbose_name_plural': 'фотографії'},
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='is_main_photo',
        ),
    ]
