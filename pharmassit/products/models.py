from django.db import models

class Product(models.Model):
    pid = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    generic_name = models.CharField(max_length=255)
    expiry_date = models.DateField()
    price = models.FloatField()
    stock = models.IntegerField()
    storage_loc = models.CharField(max_length=255)
    image = models.CharField(max_length=2083)
