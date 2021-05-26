from django.db import models
from django.contrib.auth.models import User


class ExtendedUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    email = models.EmailField(max_length=200)
    username = models.EmailField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now=True)

    flat=models.CharField(max_length=200,default=" ")
    street=models.CharField(max_length=200,default=" ")
    pincode=models.CharField(max_length=200,default=" ")
    locality=models.CharField(max_length=200,default=" ")

    def __str__(self):
        return self.username
