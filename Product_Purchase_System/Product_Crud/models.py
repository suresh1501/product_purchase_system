from django.contrib.auth.models import User
from django.db import models
    
class Product_Detail(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='images/')
    
    class Meta:
        db_table = 'product_details'