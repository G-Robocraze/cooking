import csv

recipes = []

with open('data.csv', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row
    for row in csvreader:
        recipe = {
            'recipe_name': row[0],
            'ingredients': row[1],
            'instructions': row[2]
        }
        recipes.append(recipe)

print(recipes)