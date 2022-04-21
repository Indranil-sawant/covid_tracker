from unittest.util import _MAX_LENGTH
from django.db import models

import requests

# Create your models here.



class Data(models.Model):
    name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=50)
    new_confirmed = models.IntegerField()
    total_confirmed = models.IntegerField()
    new_deaths = models.IntegerField()
    total_deaths = models.IntegerField()
    new_recovered = models.IntegerField()
    total_recovered = models.IntegerField()
    date =  models.IntegerField()

def __str__(self):
    return self.name
