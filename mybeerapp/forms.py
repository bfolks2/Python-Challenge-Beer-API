from django import forms
from django.contrib.auth.models import User
from mybeerapp.models import Beer, Rating

class BeerForm(forms.ModelForm):
    name=forms.CharField(label="Beer Name")
    abv=forms.CharField(label="ABV")
    location=forms.CharField(label="Brewery Address")

    class Meta():
        model=Beer
        exclude=['user','slug','created_at']

class RatingForm(forms.ModelForm):
    class Meta():
        model=Rating
        exclude=['user']
