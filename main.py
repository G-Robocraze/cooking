from flask import Flask, render_template, request
import pandas as pd
import random
import os
print("Current working directory:", os.getcwd())

app = Flask(__name__)

# Load the recipe dataset
recipes_df = pd.read_csv('./data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_ingredients = request.form.getlist('ingredients')
        suggested_recipes = suggest_recipes(selected_ingredients)
        return render_template('index.html', suggested_recipes=suggested_recipes)
    
    return render_template('index.html', suggested_recipes=None)

def suggest_recipes(selected_ingredients):
    suggested_recipes = []

    for _, row in recipes_df.iterrows():
        recipe_ingredients = row['ingredients'].split(',')
        if all(ingredient in recipe_ingredients for ingredient in selected_ingredients):
            suggested_recipes.append({'recipe_name': row['recipe_name'], 'ingredients': row['ingredients']})

    return suggested_recipes[:5]  # Return a limited number of suggestions


if __name__ == '__main__':
    app.run(debug=True)
