from django.db import models
from django.urls import reverse


# Create your models here.
class Request(models.Model):
    target_country = models.CharField(max_length=100)
    target_city = models.CharField(max_length=100)
    target_name = models.CharField(max_length=200)
    target_sin = models.CharField(max_length=500)

    def __str__(self):
        return self.target_sin

