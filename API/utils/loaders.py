"""Module pour charger le modèle et les données"""

import pickle
import pandas as pd


def load_data():
    df = pd.read_csv("data/segmentation_kmeans_result.csv")
    return df


def load_model():
    with open("models/olist-kmeans-current.pkl", "rb") as file:
        model = pickle.load(file)
    return model
