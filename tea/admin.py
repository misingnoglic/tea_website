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


@admin.register(Tea)
class TeaAdmin(admin.ModelAdmin):
    inlines = [PictureInline, RatingInline, CommentInline, FavoriteInline]
    list_display = ('name', 'type', 'brand', 'avg_rating', 'created_at')


for m in [TeaType, Brand, Ingredient, Picture, Rating]:
    admin.site.register(m)
