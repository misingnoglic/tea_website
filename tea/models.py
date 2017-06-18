from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


# Create your models here.

one_to_five_choices = zip( range(1,5+1), range(1,5+1) )


class TeaType(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    steeping_temperature = models.PositiveSmallIntegerField()
    steeping_time_minutes = models.PositiveSmallIntegerField()
    caffeine_level = models.PositiveSmallIntegerField(choices=one_to_five_choices)
    directions = models.TextField()

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    zip_code = models.PositiveSmallIntegerField()
    website = models.URLField()

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=60, primary_key=True)

    def __str__(self):
        return self.name


class Tea(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(TeaType)
    brand = models.ForeignKey(Brand)
    story = models.TextField()
    link = models.URLField()
    icon = models.URLField()
    ingredients = models.ManyToManyField(Ingredient)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def avg_rating(self):
        return self.rating_set.aggregate(Avg('rating'))['rating__avg']

    def __str__(self):
        return self.name


class Picture(models.Model):
    url = models.URLField()
    tea = models.ForeignKey(Tea)
    description = models.TextField()
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Picture of tea {} - {} - {}".format(self.tea, self.created_at, self.user.get_username())


class Rating(models.Model):
    rating = models.PositiveSmallIntegerField(choices=one_to_five_choices)
    tea = models.ForeignKey(Tea)
    user = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} star rating for {} by {}".format(self.rating, self.tea, self.user.get_username())

    class Meta:
        unique_together = (("user", "tea"),)


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User)
    tea = models.ForeignKey(Tea)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Favorite(models.Model):
    user = models.ForeignKey(User)
    tea = models.ForeignKey(Tea)
