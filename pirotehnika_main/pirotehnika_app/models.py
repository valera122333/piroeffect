

from django.db import models
from django.urls import reverse
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User


# Create your models here.


class Dostavka(models.Model):
    img = ImageField(upload_to="dostavka/images", verbose_name='Изображение')
    title = models.CharField(max_length=40)
    sub_title = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставка'


class Products(models.Model):
    """услуги"""
    name = models.CharField(max_length=250, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    image = models.ImageField(
        upload_to='images/cats/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'


class CategoryProducts(models.Model):
    """Категории продукции"""
    name = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField()
    description = models.TextField(
        verbose_name='Описание', null=True, blank=True)
    products = models.ManyToManyField(
        Products, verbose_name='Продукт', related_name='products')
    image = models.ImageField(
        upload_to='images/covers/', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Категория продукции'
        verbose_name_plural = 'Категории продукции'


class Orders(models.Model):
    """Заказы"""
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.CharField(max_length=100, verbose_name='Почта')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    text = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
