import pandas as pd


def read_csv(name):
    df = pd.read_csv(name)
    return df