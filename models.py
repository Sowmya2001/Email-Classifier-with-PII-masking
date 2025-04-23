

import os
import joblib

# Correct paths
model_path = "model.joblib"
vectorizer_path = "vectorizer.joblib"

# Load model and vectorizer
if os.path.exists(model_path) and os.path.exists(vectorizer_path):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
else:
    raise FileNotFoundError("Model or vectorizer file not found. Run the training script first.")

def classify_email(email_text: str) -> str:
    """Classifies an email into its category."""
    vectorized_text = vectorizer.transform([email_text])
    prediction = model.predict(vectorized_text)
    return prediction[0]


