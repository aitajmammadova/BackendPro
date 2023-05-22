from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=300)
    brand=models.ForeignKey("brands.Brand", on_delete=models.CASCADE)
    price=models.FloatField(blank=True,null=True)
    def __str__(self):
        return self.name