from django.db import models
from django.contrib import auth
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

# class User(auth.models.User, auth.models.PermissionsMixin):
#
#     def __str__(self):
#         return "@{x}".format(x=self.username) #username is a built in attribute from auth.models.User
