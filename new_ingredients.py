import csv

if __name__=="__main__":
    r = csv.reader(open("ingredient_legend.csv"))
    old_ingredients = set()
    for line in r:
        old_ingredients.add(line[0])

    new_ingredients = set()
    for line in open("ingredients_match.csv"):
        new_ingredients.add(line.strip())

    for ing in new_ingredients - old_ingredients:
        print(ing)

