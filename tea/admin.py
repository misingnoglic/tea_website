from django.contrib import admin
from .models import Tea, TeaType, Brand, Ingredient, Picture, Rating

# Register your models here.
for m in [Tea, TeaType, Brand, Ingredient, Picture, Rating]:
    admin.site.register(m)
