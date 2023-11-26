from django.db import models
from django.urls import reverse


# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Plant(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=100)
    description = models.TextField(default="") 
    image_url = models.URLField(default="")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class PlantCreate(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255,default="")
    description = models.TextField(default="") 
    image_url = models.URLField(default="")

    def get_absolute_url(self):
       return reverse('UserInput', kwargs={'pk': self.pk})
class UserInput(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255,default="")
    description = models.TextField(default="") 
    image_url = models.URLField(default="")
    def get_absolute_url(self):
        return reverse('')