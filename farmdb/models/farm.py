from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone

class Farm(models.Model):
    name = models.CharField(max_length=100, verbose_name='Farm name')
    address = models.CharField(max_length=150, verbose_name='Farm address')
    active = models.BooleanField(default=True, verbose_name='Farm active')
    date_of_creation = models.DateField(auto_created=timezone.now, verbose_name='Date of record creation')

    def __str__(self):
        return self.name


class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'active', 'date_of_creation')
    search_fields = ('name', 'address')
    list_filter = ('active',)
    date_hierarchy = 'date_of_creation'
    ordering = ('-date_of_creation',)


class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None,null=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    active = models.BooleanField(default=False, verbose_name='Farmer active')
    reg_date = models.DateField(auto_created=timezone.now, verbose_name='Date of registration for farmer')

    def __str__(self):
        return self.user.last_name + ', ' + self.user.first_name


class FarmerAdmin(admin.ModelAdmin):
    list_display = ('user', 'farm', 'gender', 'active', 'reg_date')
    search_fields = 'farm'
    list_filter = ('active',)
    date_hierarchy = 'reg_date'
    ordering = ('-reg_date', 'user__last_name', 'user__first_name')