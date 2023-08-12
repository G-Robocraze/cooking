from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load your dataset into a Pandas DataFrame
df = pd.read_csv("main.csv")
df['ingredients'] = df['ingredients'].apply(eval)  # Convert the string representation back to lists

# Load the ingredients list from another CSV file
ingredients_list = pd.read_csv("unique_ingredients.csv")["ingredient"].tolist()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_ingredients = [ingredient.lower() for ingredient in request.form.getlist("ingredients")]
        suggested_recipes = generate_suggested_recipes(selected_ingredients)
        return render_template("index.html", ingredients=ingredients_list, suggested_recipes=suggested_recipes)
    return render_template("index.html", ingredients=ingredients_list, suggested_recipes=[])

def generate_suggested_recipes(selected_ingredients):
    filtered_df = df[df["ingredients"].apply(lambda x: all(ingredient.lower() in x for ingredient in selected_ingredients))]
    suggested_recipes = filtered_df[["name", "description"]].values.tolist()
    return suggested_recipes

if __name__ == "__main__":
    app.run(debug=True)
