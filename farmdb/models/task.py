from django.db import models
from django.contrib import admin
from django.utils import timezone

from .farm import Farm
from .animalData import AnimalGroup,SubGroup

class Task(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    task = models.CharField(max_length=50)
    active = models.BooleanField(default=True)


class TaskMaster(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    comments = models.TextField()
    animalGroup = models.ForeignKey(AnimalGroup, on_delete=models.CASCADE)
    sub_group = models.ForeignKey(SubGroup, on_delete=models.CASCADE)
    workers = models.IntegerField()
    minutes = models.IntegerField()
    complete = models.BooleanField(default=False)


class TaskRecurring(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_date = models.DateField()
    comments = models.TextField()
    animalGroup = models.ForeignKey(AnimalGroup, on_delete=models.CASCADE)
    sub_group = models.ForeignKey(SubGroup, on_delete=models.CASCADE)
    workers = models.IntegerField()
    minutes = models.IntegerField()
    recur = models.CharField(max_length=15)
