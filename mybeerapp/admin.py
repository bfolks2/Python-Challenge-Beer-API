from django.contrib import admin
from mybeerapp import models

# Register your models here.

admin.site.register(models.Beer)
admin.site.register(models.Glass)
admin.site.register(models.Rating)
