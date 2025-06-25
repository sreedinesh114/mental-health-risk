import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(path):
    df = pd.read_csv(path)
    df = df.drop(columns=["user_id"])

    # Convert 'yes'/'no' to 1/0
    df['mental_risk'] = df['mental_risk'].map({'yes': 1, 'no': 0})
    return df

def split_features_labels(df):
    X = df.drop("mental_risk", axis=1)
    y = df["mental_risk"]
    return X, y