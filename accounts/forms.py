from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserCreateForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')

# class UserCreateForm(UserCreationForm):
#     class Meta():
#         model = get_user_model()
#         fields = ('username','email','password1','password2')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args,**kwargs)
#         self.fields['username'].label = 'UserName'
#         self.fields['email'].label = 'Email Address'
