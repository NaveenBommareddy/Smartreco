# app.py
from flask import Flask, render_template, redirect, url_for
from db import load_products, load_interactions
from model import SmartRecoModel
import pandas as pd

app = Flask(__name__)

# Load data
products = load_products()
interactions = load_interactions()

# Initialize recommendation model
reco_model = SmartRecoModel(interactions)

@app.route("/")
def home():
    return render_template("home.html", products=products.to_dict(orient="records"))

@app.route("/track_product/<int:product_id>")
def track_product(product_id):
    global interactions
    # For now assume user_id = 1
    user_id = 1
    new_entry = pd.DataFrame({
        "user_id": [user_id],
        "product_id": [product_id],
        "interaction": [1]
    })
    interactions = pd.concat([interactions, new_entry], ignore_index=True)
    
    # Retrain model with updated interactions
    reco_model.interactions_df = interactions
    reco_model.train_model()
    
    return redirect(url_for('recommendations'))

@app.route("/recommendations")
def recommendations():
    user_id = 1  # Assuming one user
    recommended = reco_model.recommend(user_id=user_id, products_df=products)
    return render_template("recommendations.html", recommendations=recommended.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)

