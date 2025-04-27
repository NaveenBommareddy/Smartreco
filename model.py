from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import pandas as pd

class SmartRecoModel:
    def __init__(self, interactions_df):
        self.interactions_df = interactions_df
        self.model = None
        self.train_model()

    def train_model(self):
        reader = Reader(rating_scale=(0, 1))
        data = Dataset.load_from_df(self.interactions_df[['user_id', 'product_id', 'interaction']], reader)
        trainset = data.build_full_trainset()
        self.model = SVD()
        self.model.fit(trainset)

    def recommend(self, user_id, products_df, top_n=3):
        all_product_ids = products_df['product_id'].tolist()
        predictions = [(pid, self.model.predict(user_id, pid).est) for pid in all_product_ids]
        predictions.sort(key=lambda x: x[1], reverse=True)
        recommended_ids = [pid for pid, _ in predictions[:top_n]]
        recommended_products = products_df[products_df['product_id'].isin(recommended_ids)]
        return recommended_products

# For quick testing
if __name__ == "__main__":
    from db import load_products, load_interactions

    products = load_products()
    interactions = load_interactions()

    reco_model = SmartRecoModel(interactions)
    recommendations = reco_model.recommend(user_id=1, products_df=products)
    print(recommendations)
