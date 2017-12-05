import csv
import datetime
from django.core.exceptions import ObjectDoesNotExist
from tea_website.settings import BASE_DIR
import progressbar

import os
from django.db import transaction

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tea_website.settings")
import django
django.setup()

from tea.models import Ingredient, Tea
from django.conf import settings

ingredients = csv.DictReader(open('ingredient_legend.csv', encoding='utf8'))

bar = progressbar.ProgressBar(max_value=500)

with transaction.atomic():
    for line in bar(ingredients):
        name = line["Name"].lower().strip()
        ing = Ingredient.objects.get(name=name)
        if line["Copy Of"]:
            orig = Ingredient.objects.get(name=line["Copy Of"].lower().strip())
            teas = Tea.objects.filter(ingredients=ing)
            for tea in teas:
                tea.ingredients.remove(ing)
                tea.ingredients.add(orig)
                tea.save()
            ing.delete()
        else:
            if line["Flavor"]:
                ing.flavoring = True
            if line["Base"]:
                try:
                    base_ing = Ingredient.objects.get(name=line["Base"].lower().strip())
                except ObjectDoesNotExist:
                    base_ing = Ingredient(name=line["Base"].lower().strip())
                    base_ing.save()
                ing.base = base_ing
            ing.save()

names = [x.name for x in Ingredient.objects.all()]
os.system("del ingredients_match.csv")
with open("ingredients_match.csv", "w") as f:
    for i in names: print(i, file=f)