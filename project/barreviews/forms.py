from django import forms

from barreviews.models import *

class BarForm(forms.ModelForm):
    class Meta:
        model = Bar

class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink

class UserForm(forms.ModelForm):
    class Meta:
        model = User