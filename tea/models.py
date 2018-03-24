from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


# Create your models here.

zero_to_five_choices = list(zip(range(0, 5 + 1), range(0, 5 + 1)))


class TeaType(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    steeping_temperature = models.PositiveSmallIntegerField()
    steeping_time_minutes = models.PositiveSmallIntegerField()
    caffeine_level = models.PositiveSmallIntegerField(choices=zero_to_five_choices)
    directions = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    zip_code = models.PositiveSmallIntegerField(default=0)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=60, primary_key=True)
    flavoring = models.BooleanField(default=False) # E.g. is it cherry flavoring
    # For ingredients with differing names but same idea (raspberries vs raspberry)
    base = models.ForeignKey("Ingredient", related_name="base_ingredient", null=True)

    def __str__(self):
        return self.name

    @property
    def is_base(self):
        return self.base == None

    class Meta:
        ordering = ['name']

class Tea(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(TeaType)
    brand = models.ForeignKey(Brand, blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    icon = models.URLField(blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='teas')
    steeping_time_minutes = models.PositiveSmallIntegerField(blank=True, null=True)
    steeping_temperature_f = models.PositiveSmallIntegerField(blank=True, null=True)
    description_directions = models.CharField(max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def avg_rating(self):
        return self.rating_set.aggregate(Avg('rating'))['rating__avg']

    def __str__(self):
        return self.name

    def str_ingredients(self):
        return ", ".join([ing.name for ing in Ingredient.objects.filter(teas=self)])

class Picture(models.Model):
    url = models.URLField()
    tea = models.ForeignKey(Tea)
    description = models.TextField()
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Picture of tea {} - {} - {}".format(self.tea, self.created_at, self.user.get_username())


class Rating(models.Model):
    tea = models.ForeignKey(Tea)
    rating = models.PositiveSmallIntegerField(choices=zero_to_five_choices)
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
