from flask import Flask, render_template, request
import pandas as pd
import random
import os
import csv
print("Current working directory:", os.getcwd())

app = Flask(__name__)

# Load the recipe dataset
recipes_df = csv.reader('./data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_ingredients = request.form.getlist('ingredients')
        suggested_recipes = suggest_recipes(selected_ingredients)
        return render_template('index.html', suggested_recipes=suggested_recipes)
    
    return render_template('index.html', suggested_recipes=None)

def suggest_recipes(selected_ingredients):
    suggested_recipes = []

    with open('data.csv', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            recipe_ingredients = row[1].split(',')
            if all(ingredient in recipe_ingredients for ingredient in selected_ingredients):
                suggested_recipes.append({'recipe_name': row[0], 'ingredients': row[1]})

    return suggested_recipes[:5]  # Return a limited number of suggestions



if __name__ == '__main__':
    app.run(debug=True)
