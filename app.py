from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load your recipes data
recipes_data = pd.read_csv("dataset_recipe.csv")

# Load unique ingredients from unique_incredients.csv
unique_ingredients = pd.read_csv("unique_ingredients.csv")["ingredient"].tolist()

# Replace with your prediction method
def get_recipes(selected_ingredients):
    # Perform your prediction using selected_ingredients
    # For example, you can modify this to use your existing method
    filtered_recipes = recipes_data[recipes_data["ingredients"].apply(lambda x: all(ing in x for ing in selected_ingredients))]
    suggested_recipes = filtered_recipes[["name", "steps","ingredients"]].values.tolist()
    return suggested_recipes
@app.route('/')
def index():
    unique_ingredients = pd.read_csv("unique_ingredients.csv")["ingredient"].tolist()
    unique_ingredients.sort()  # Sort the ingredients alphabetically
    return render_template('index.html', unique_ingredients=unique_ingredients)
# @app.route("/", methods=["GET"])
# def index():
#     return render_template("index.html", unique_ingredients=unique_ingredients)

@app.route("/get_recipes", methods=["POST"])
def get_recipes_route():
    data = request.get_json()
    selected_ingredients = data["ingredients"]
    recipe_list = get_recipes(selected_ingredients)
    return jsonify({"recipes": recipe_list})

if __name__ == "__main__":
    app.run(debug=True)
