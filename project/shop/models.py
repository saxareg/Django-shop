from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    discription = models.CharField(max_length=2000)
    amount = models.IntegerField()
    price = models.IntegerField()
    tipe = models.CharField(max_length=255)



