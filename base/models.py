from django.db import models
from django.contrib.auth.models import AbstractUser

import os

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.PositiveIntegerField(null=True)
    state = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, upload_to='topic/')

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super(Topic, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150,null=True)
    bio = models.CharField(max_length=1000,null=True)
    image = models.ImageField(null=True, upload_to='product/')
    price = models.PositiveIntegerField(null=True)
    stock = models.PositiveIntegerField(null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    cost = models.PositiveIntegerField(null=True)
    discount = models.PositiveIntegerField(null=True)
    priceDiscount = models.PositiveIntegerField(null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super(Product, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name

    class Meta:
        order_with_respect_to = 'discount'

class Banner(models.Model):

    title = models.CharField(max_length=150,null=True)
    type = models.CharField(max_length=150,null=True)
    message = models.CharField(max_length=150,null=True)
    image = models.ImageField(null=True, upload_to='banner/')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    minPrice = models.PositiveIntegerField(null=True)
    maxPrice = models.PositiveIntegerField(null=True)
    minDiscount = models.PositiveIntegerField(null=True)
    

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super(Topic, self).delete(*args, **kwargs)
    
    def __str__(self):
        return self.title
    