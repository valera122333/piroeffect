

from django.db import models

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
