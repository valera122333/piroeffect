# Generated by Django 3.2.9 on 2022-04-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pirotehnika_app', '0012_categoryproducts_orders_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryproducts',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
