import pandas as pd

def load_csv(filepath):
    return pd.read_csv(filepath)

def save_csv(dataframe, filepath):
    dataframe.to_csv(filepath, index=False)
