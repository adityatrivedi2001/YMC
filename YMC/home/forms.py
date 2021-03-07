from django import forms
from . import models


class contactusForm(forms.Form):
    name = forms.CharField(label="Enter name", max_length=10)
    email = forms.EmailField(label="Enter Email")
    file = forms.TextField()  
