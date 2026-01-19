import pandas as pd

url = ("https://breathecode.herokuapp.com/asset/internal-link?id=927&path=AB_NYC_2019.csv")

def load_data():
    return pd.read_csv(url)