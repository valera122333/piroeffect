

from django.db import models

from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User

from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    content = models.TextField(blank=True, verbose_name="описание")
    photo = models.ImageField(
        upload_to="product/images", verbose_name="Фото")
    price = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name='Цена')
    cat = models.ForeignKey(
        "Category", on_delete=models.PROTECT, verbose_name="Категории"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

    class Meta:
        verbose_name = "Арты и биографии"
        verbose_name_plural = "Арты и биографии"
        ordering = ["title"]


class Category(models.Model):
    name = models.CharField(
        max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    cat_photo = models.ImageField(
        upload_to="categories/images", verbose_name="Фото")

    def __str__(self):
        return (
            self.name
        )  # В результате, в таблице category будет два индексируемых поля: id и name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

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
