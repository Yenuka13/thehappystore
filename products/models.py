from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    stock = models.IntegerField()
    img_url = models.CharField(max_length=2083)
    download_url = models.CharField(max_length=10000000000000000000000000000000000000)
