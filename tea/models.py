from django.db import models
from django.contrib.auth.models import User

# Create your models here.

one_to_five_choices = zip( range(1,5+1), range(1,5+1) )


class TeaType(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    steeping_temperature = models.PositiveSmallIntegerField()
    steeping_time_minutes = models.PositiveSmallIntegerField()
    caffeine_level = models.PositiveSmallIntegerField(choices=one_to_five_choices)
    directions = models.TextField()


class Brand(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    zip_code = models.PositiveSmallIntegerField()
    website = models.URLField()


class Ingredient(models.Model):
    name = models.CharField(max_length=60, primary_key=True)


class Tea(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(TeaType)
    brand = models.ForeignKey(Brand)
    story = models.TextField()
    link = models.URLField()
    icon = models.URLField()
    ingredients = models.ManyToManyField(Ingredient)


class Picture(models.Model):
    url = models.URLField()
    tea = models.ForeignKey(Tea)
    description = models.TextField()
    user = models.ForeignKey(User)


class Rating(models.Model):
    rating = models.PositiveSmallIntegerField(choices=one_to_five_choices)
    tea = models.ForeignKey(Tea)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = (("user", "tea"),)
