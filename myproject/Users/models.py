from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    brands = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Shoe(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='shoe_images/')

    def __str__(self):
        return self.brand

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shoe_size = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"