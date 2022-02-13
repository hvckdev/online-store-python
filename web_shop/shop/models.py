from django.conf import settings
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.name


class Order(models.Model):
    SIZE_CHOICES = (
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.CharField(max_length=256)
    size = models.CharField(max_length=256, choices=SIZE_CHOICES)
    tracking_number = models.TextField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return 'Delivered' if self.status == 1 else 'On the way'
