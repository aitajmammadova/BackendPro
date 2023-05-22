from django.db import models

# Create your models here.
class Store(models.Model):
    name=models.CharField(max_length=400)
    address=models.TextField()
    products=models.ManyToManyField("products.Product", blank=True)
    
    def __str__(self):
        return self.name