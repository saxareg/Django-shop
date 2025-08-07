from django.db import models


# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    discription = models.CharField(max_length=2000)
    amount = models.IntegerField()
    price = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
