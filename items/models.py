from django.db import models
from actors.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='pics/')
    category = models.ForeignKey(Category, related_name='items', on_delete = models.CASCADE,)

    def __str__(self):
        return self.name

class Favourite(models.Model):
    item = models.ForeignKey(Item, related_name='favourite', on_delete = models.CASCADE,)
    user = models.ForeignKey(User, on_delete = models.CASCADE,)


