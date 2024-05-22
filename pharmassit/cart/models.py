from django.db import models
from products.models import Product

class Cart(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    pid = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)    
    price = models.FloatField(null=True)
    tot_price = models.FloatField(null=True)
    
