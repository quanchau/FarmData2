from django.db import models
from django.contrib import admin
from django.utils import timezone

from .farm import Farm

class Task(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    task = models.CharField(max_length=50)
    active = models.BooleanField(default=True)



