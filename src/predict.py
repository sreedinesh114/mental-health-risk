import numpy as np
from joblib import load

def predict_risk(age, stress_level, sleep_quality):
    model = load("models/model.joblib")
    input_data = np.array([[age, stress_level, sleep_quality]])
    return model.predict(input_data)[0]
