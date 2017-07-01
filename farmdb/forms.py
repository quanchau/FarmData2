from .models import *
from django import forms
from django.contrib.auth.models import User

class FarmerForm(forms.ModelForm):

    class Meta:
        model = Farmer
        fields = [Far]