# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.svm import LinearSVC
# from joblib import dump

# def train_model():
#     df = pd.read_csv("data/emails.csv")
#     X = df['email']
#     y = df['type']

#     vectorizer = TfidfVectorizer(stop_words='english')
#     X_vect = vectorizer.fit_transform(X)

#     clf = LinearSVC()
#     clf.fit(X_vect, y)

#     dump(vectorizer, "saved_models/vectorizer.joblib")
#     dump(clf, "saved_models/model.joblib")

import os
import joblib

# Correct paths
model_path = "saved_models/model.joblib"
vectorizer_path = "saved_models/vectorizer.joblib"

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


