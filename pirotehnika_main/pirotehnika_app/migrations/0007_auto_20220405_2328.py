# Generated by Django 3.2.9 on 2022-04-05 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pirotehnika_app', '0006_auto_20220405_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cat',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]