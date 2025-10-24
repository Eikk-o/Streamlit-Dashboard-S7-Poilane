import pandas as pd

def load_raw_data():
    return pd.read_csv("data/paris2024-athletes.csv", sep=";")