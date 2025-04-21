import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

# Load your dataset (update the filename if needed)
data = pd.read_csv("emails.csv")  # Replace with your actual filename

# Use the correct column names
X = data["email"]
y = data["type"]

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the email text
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Train the classifier
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Create directory to save models
os.makedirs("saved_models", exist_ok=True)

# Save vectorizer and model
joblib.dump(vectorizer, "saved_models/vectorizer.joblib")
joblib.dump(model, "saved_models/email_classifier_model.joblib")

print("✅ Training complete! Files saved in 'saved_models/'")
