# Import teas from CSV to database
# Running this will delete the database
import csv
import datetime
from django.core.exceptions import ObjectDoesNotExist
from tea_website.settings import BASE_DIR
import progressbar

import os
os.system("del db.sqlite3")
os.system("del tea\\migrations\\0*")

os.system("python manage.py makemigrations")
os.system("python manage.py migrate")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tea_website.settings")
import django
django.setup()

from tea_combiner import combine

from tea.models import *
from django.conf import settings

# Add the tea types:
# times from http://www.artoftea.com/what-is-tea/recommended-steep-times/
# caffine from https://spoonuniversity.com/lifestyle/how-much-caffeine-is-actually-in-your-tea
# but also made up a little by me

# each is a list, caffeine level 0-5, steeping temp, and steeping time
types = {"Pu'erh": [4,195, 4],
         'White': [1,180, 2],
         'Herbal': [0,212, 8],
         'Matcha': [2,170, 3],
         'Chai': [5,212, 3],
         'Green': [2,183, 3],
         'Black': [5,212, 4],
         'Oolong': [4,195, 4],
         'Rooibos': [0,212, 5],
         'Mate': [3, 180, 5],
}
for name, (caffeine, temp, time) in types.items():
    new_type = TeaType()
    new_type.name = name
    new_type.steeping_temperature = temp
    new_type.caffeine_level = caffeine
    new_type.steeping_time_minutes = time
    new_type.save()

teas = csv.DictReader(open('teas.csv', encoding='utf8'))

bar = progressbar.ProgressBar(max_value=200)

for line in bar(teas):
    new_tea = Tea()
    new_tea.name = line['Name'].strip().title()
    type = line["Type (Black/White/Green/etc...)"].strip().capitalize()
    type_obj = TeaType.objects.get(name=type)
    new_tea.type = type_obj

    brand = line['Brand'].strip()
    try:
        brand_obj = Brand.objects.get(name=brand)
    except ObjectDoesNotExist:
        brand_obj = Brand(name=brand)
        brand_obj.save()
    new_tea.brand = brand_obj
    new_tea.story = line["Story"]
    new_tea.link = line["Link"]
    if line["Steeping Time (mins)"]: new_tea.steeping_time_minutes = int(line["Steeping Time (mins)"].strip())
    if line["Water Temperature (F)"]: new_tea.steeping_temperature_f = int(line["Water Temperature (F)"].strip())
    new_tea.description_directions = line["Description/Directions"].strip()
    new_tea.save()

    # After new_tea is created
    ingredients = line["Ingredients (comma separated)"].split(",")
    ingredients = [i.strip().lower().strip(".") for i in ingredients]
    for ing in ingredients:
        if ing:
            try:
                ing_obj = Ingredient.objects.get(name=ing)
            except ObjectDoesNotExist:
                ing_obj = Ingredient(name=ing)
                ing_obj.save()
            new_tea.ingredients.add(ing_obj)

combine()

names = [x.name for x in Ingredient.objects.all()]
os.system("del ingredients_match.csv")
with open("ingredients_match.csv", "w") as f:
    for i in names:
        print(i, file=f)
