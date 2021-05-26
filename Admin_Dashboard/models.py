from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class HomeImage(models.Model):
    image = models.ImageField(upload_to="HomeImages")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FeaturedImage(models.Model):
    image = models.ImageField(upload_to="FeaturedImages")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OM(models.Model):
    no_of_meal = models.CharField(max_length=100)
    orderId = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    snack = models.CharField(max_length=100)
    breakfast = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="Placed")
    address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,unique=False)

    def __str__(self):
        return self.orderId


class OT(models.Model):
    orderId = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    vegOrJain = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="Placed")
    user = models.ForeignKey(User, on_delete=models.CASCADE,unique=False)
    address = models.TextField()
    # snack=models.CharField(max_length=100)

    def __str__(self):
        return self.orderId
