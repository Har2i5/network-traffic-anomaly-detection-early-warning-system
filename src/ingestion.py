import pandas as pd

def load_data(filepath):

    df = pd.read_csv(filepath)

    df['date'] = pd.to_datetime(df['date'])

    return df