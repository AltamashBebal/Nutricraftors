from django.db import models
from django.contrib.auth.models import User


class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    query = models.TextField()
    contact = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ExtendedUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    email = models.EmailField(max_length=200)
    username = models.EmailField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now=True)

    flat = models.CharField(max_length=200,default="flat")
    # stret = models.CharField(max_length=200,default=True)
    # pincode = models.CharField(max_length=200,default=True)
    # location = models.CharField(max_length=200,default=True)

    def __str__(self):
        return self.first_name


class Subscriber(models.Model):
    email = models.CharField(max_length=200)
    created = models.CharField(max_length=100)

    def __str__(self):
        return self.email
