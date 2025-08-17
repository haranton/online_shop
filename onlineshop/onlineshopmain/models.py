from django.db import models
from django.core.files.storage import default_storage

class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500)
    discription = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(storage=default_storage, upload_to='', default="")

    def __str__(self):
        return self.name
