# Generated by Django 3.1.4 on 2020-12-12 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20200912_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=200, null=True, verbose_name='назва'),
        ),
    ]
