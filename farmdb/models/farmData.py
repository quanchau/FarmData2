from django.db import models
from django.contrib import admin
from django.utils import timezone

from .farm import Farm,Farmer
from .task import Task


#Check if this is required
class Field_GH(models.Model):
    size = models.DecimalField(max_digits=8,decimal_places=2)
    numberOfBeds = models.DecimalField(max_digits=5,decimal_places=2)#I think this sound be integer
    length = models.DecimalField(max_digits=8,decimal_places=2)
    active = models.BooleanField(default=True)

class Plant(models.Model):
    crop = models.CharField(max_length=30)
    units = models.CharField(max_length=30)
    units_per_case =models.FloatField()
    dh_units = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

class labor(models.Model):
    ##The farmer who created the labor job? Or is it for the laborer himself?
    farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    #Labor add date?
    ldate=models.DateField()
    crop=models.CharField(max_length=30)
    #Pretty sure this needs to be a FK for field_GH
    fieldID=models.CharField(max_length=30)
    # Need to create a Task class
    task = models.ForeignKey(Task)
    hours = models.DecimalField(max_digits=8,decimal_places=2)
    comments = models.TextField()

class flat(models.Model):
    cells = models.IntegerField()

    def __str__(self):
        return str(self.cells)

class transferred_to(models.Model):
    farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    field=models.ForeignKey(Field_GH,on_delete=models.CASCADE)
    crop= models.ForeignKey(Plant,on_delete=models.CASCADE)
    fieldID=models.CharField(max_length=30)
    bedft=models.DecimalField(max_digits=8,decimal_places=2)
    comments=models.TextField()
    rowsBed = models.PositiveIntegerField()
    hours = models.DecimalField(max_digits=8,decimal_places=2)
    gen = models.IntegerField(default=1)
    annual = models.BooleanField(default=True)
    lastHarvest = models.DateField()

class harvested(models.Model):
    farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    harvestDate=models.DateField()
    crop = models.ForeignKey(Plant,on_delete=models.CASCADE)
    field = models.ForeignKey(Field_GH,on_delete=models.CASCADE)
    produce = models.DecimalField(max_digits=8,decimal_places=2)
    comments = models.TextField()
    hours = models.DecimalField(max_digits=8,decimal_places=2)
    unit = models.CharField(max_length=30)
    gen = models.IntegerField()

class comments(models.Model):
    farmer = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    commentDate= models.DateField(auto_created=timezone.now)
    comments = models.TextField()
    filename = models.FileField(default=None,null=True)

class gh_seeding(models.Model):
    farmer = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    crop = models.ForeignKey(Plant,on_delete=models.CASCADE)
    seedDate = models.DateField()
    #Why are there two flat references?
    flats = models.DecimalField(max_digits=8,decimal_places=2)
    cellsFlat = models.IntegerField()
    gen = models.IntegerField(default=1)
    numseeds_planted = models.PositiveIntegerField()
    comments = models.TextField()
    varieties = models.TextField()

    class Meta:
        unique_together=('crop','seedDate','varieties')

class extUnits(models.Model):
    unit =models.CharField(max_length=30)

class Tools(models.Model):
    tool_name=models.CharField(max_length=30)
    type = models.CharField(max_length=30)

class Harvest(models.Model):
    farm=models.ForeignKey(Farm, on_delete=models.CASCADE)
    comment=models.TextField()



class Target(models.Model):
    targetName = models.CharField(max_length=30)
    prefix = models.CharField(max_length=20)
    nextNum = models.SmallIntegerField(default=1)
    active = models.BooleanField(default=True)

class TargetEmail(models.Model):
    email = models.EmailField()
    target = models.ForeignKey(Target,on_delete=models.CASCADE)

class HarvestListItem(models.Model):
    crop = models.ForeignKey(Plant,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8,decimal_places=2)
    units = models.CharField(max_length=10)
    harvestList = models.ForeignKey(Harvest,on_delete=models.CASCADE)
    target = models.ForeignKey(Target,models.CASCADE)




