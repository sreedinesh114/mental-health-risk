from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from joblib import dump

from preprocess import load_data, split_features_labels

# Load and preprocess
df = load_data("data/mental_health_risk_prediction.csv")
X, y = split_features_labels(df)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
dump(model, "models/model.joblib")
print("✅ Model saved to models/model.joblib")
