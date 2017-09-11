from django import forms
from django.contrib.auth.models import User
from mybeerapp.models import Beer

class BeerForm(forms.ModelForm):
    name=forms.CharField(label="Beer Name")
    abv=forms.CharField(label="ABV")
    location=forms.CharField(label="Brewery Address")

    class Meta():
        model=Beer
        exclude=['user','slug']
