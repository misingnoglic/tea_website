from django.contrib import admin
from .models import Tea, TeaType, Brand, Ingredient, Picture, Rating, Comment, Favorite

# Register your models here.

class PictureInline(admin.TabularInline):
    model = Picture

class RatingInline(admin.StackedInline):
    model = Rating

class CommentInline(admin.TabularInline):
    model = Comment

class FavoriteInline(admin.TabularInline):
    model = Favorite

class IngredientInline(admin.TabularInline):
    model = Ingredient


@admin.register(Tea)
class TeaAdmin(admin.ModelAdmin):
    inlines = [PictureInline, RatingInline, CommentInline, FavoriteInline]
    list_display = ('name', 'type', 'brand', 'avg_rating', 'created_at')
    list_filter = ['type', 'brand']
    search_fields = ['name', 'ingredients__name']

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]
    list_display = ('name', 'flavoring', 'base', 'is_base')
    search_fields = ['name', 'base__name']
    list_filter = ['flavoring']

for m in [TeaType, Brand, Picture, Rating]:
    admin.site.register(m)
