from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_id = models.BigIntegerField()
    discription = models.CharField(max_length=200)
    brand = models.CharField(max_length=25)
    category = models.CharField(max_length=30)
    product_link = models.URLField(max_length=150)

class InputField(models.Model):
    input_id_list = models.TextField(max_length=200)

