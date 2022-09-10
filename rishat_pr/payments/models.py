from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    description = models.CharField(max_length=30, verbose_name='Описание')
    price = models.FloatField(default=0, verbose_name='Цена')
