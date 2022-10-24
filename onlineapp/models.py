from statistics import mode
from django.db import models

# Create your models here.
class Addcategory(models.Model):
    name=models.CharField(max_length=30)
class Addbrand(models.Model):
    name=models.CharField(max_length=30)
