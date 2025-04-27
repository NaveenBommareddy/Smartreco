import pandas as pd

def load_products(filepath="C:\Users\navee\OneDrive\Desktop\smartreco\data\products.csv"):
    products = pd.read_csv(filepath)
    return products

def load_interactions(filepath="C:\Users\navee\OneDrive\Desktop\smartreco\data\interactions.csv"):
    interactions = pd.read_csv(filepath)
    return interactions
