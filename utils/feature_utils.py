import pandas as pd

def create_features(data):
    # Example feature engineering
    data['feature_sum'] = data.sum(axis=1)
    return data
