from .models import *
from django import forms
from django.contrib.auth.models import User



class FarmerForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password','email']

class AnimalGroupForm(forms.ModelForm):

    class Meta:
        model = AnimalGroup
        fields = ['farm', 'animalGroup','active']