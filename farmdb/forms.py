from .models import *
from django import forms
from django.contrib.auth.models import User



class Create_Farmer_Form(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password','email']

class Animal_Group_Form(forms.ModelForm):

    class Meta:
        model = Breed
        fields = ['farm', 'animalGroup','active']