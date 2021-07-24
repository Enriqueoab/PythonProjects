from django.db import models
from django.db.models.fields import CharField

class Product(models.Model):
    name= models.CharField(max_length=255) # Field that contain text data
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2038)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description =models.CharField(max_length=255)
    discount = models.FloatField()

