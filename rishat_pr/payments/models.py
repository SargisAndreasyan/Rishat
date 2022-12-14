from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    description = models.CharField(max_length=30, verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)
