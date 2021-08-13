from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
   

class Characteristic(models.Model):
    name = models.CharField(max_length=255)

class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=255)
    group = models.ForeignKey("Group", on_delete=CASCADE, related_name="animals")
    characteristics = models.ManyToManyField(Characteristic)

