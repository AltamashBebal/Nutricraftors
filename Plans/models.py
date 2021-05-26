from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TransformationPlan(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    description = models.TextField()
    minidescription = models.TextField(default="Mini")
    weeks = models.IntegerField()
    image = models.ImageField(upload_to='Transformation')

    def __str__(self):
        return self.name

class MealBox(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='MealBox')
    def __str__(self):
        return self.name


    


