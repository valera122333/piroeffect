# Generated by Django 3.2.9 on 2022-04-05 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pirotehnika_app', '0007_auto_20220405_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('cat_photo', models.ImageField(upload_to='categories/images', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='описание')),
                ('photo', models.ImageField(upload_to='product/images', verbose_name='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pirotehnika_app.category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Арты и биографии',
                'verbose_name_plural': 'Арты и биографии',
                'ordering': ['title'],
            },
        ),
    ]