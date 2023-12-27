from django.db import models

# Create your models here.
class Products(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    description = models.TextField()
