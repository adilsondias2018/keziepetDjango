from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    animal = models.ForeignKey("Animal", on_delete=CASCADE)

class Characteristic(models.Model):
    name = models.CharField(max_length=255)

class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=255)
    characteristics = models.ManyToManyField(Characteristic)

