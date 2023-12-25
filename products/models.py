from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()