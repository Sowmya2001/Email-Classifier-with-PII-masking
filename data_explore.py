import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib
import os

# Load your dataset
df = pd.read_csv("emails.csv")  # Replace with actual filename

# Check column names
print("Columns:", df.columns.tolist())

# Assume "email" and "category" are the columns
texts = df["email"]  # Column containing email text
labels = df["type"]  # Column containing target labels

# Split for a simple model (you can skip this if not training)
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Create a pipeline: Tfidf + Classifier
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", MultinomialNB())
])

# Train the model
pipeline.fit(X_train, y_train)

# Save vectorizer and model
os.makedirs("saved_models", exist_ok=True)
joblib.dump(pipeline.named_steps["tfidf"], "saved_models/vectorizer.joblib")
joblib.dump(pipeline.named_steps["clf"], "saved_models/model.joblib")

print("✅ Vectorizer and model saved in 'saved_models/' folder.")


