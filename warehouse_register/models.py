from django.db import models

# Create your models here.

class Goods(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

