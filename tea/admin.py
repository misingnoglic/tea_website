from django.contrib import admin
from .models import Tea, TeaType, Brand, Ingredient, Picture, Rating

# Register your models here.

class IngredientInline(admin.TabularInline):
    model = Ingredient

class PictureInline(admin.TabularInline):
    model = Picture

class RatingInline(admin.TabularInline):
    model = Rating

@admin.register(Tea)
class TeaAdmin(admin.ModelAdmin):
    inlines = [PictureInline, RatingInline]
    list_display = ('name', 'type', 'brand', 'avg_rating', 'created_at')


for m in [TeaType, Brand, Ingredient, Picture, Rating]:
    admin.site.register(m)
