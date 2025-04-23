from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
from utils import mask_pii
import os

# Load vectorizer and model
vectorizer_path = "vectorizer.joblib"
model_path = "model.joblib"

if not os.path.exists(vectorizer_path) or not os.path.exists(model_path):
    raise FileNotFoundError("Model or vectorizer not found!")

vectorizer = joblib.load(vectorizer_path)
model = joblib.load(model_path)
print("✅ Vectorizer and model loaded successfully!")

# Initialize FastAPI app
app = FastAPI()

# Base route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Email Classification API!"}

# Request body model
class EmailInput(BaseModel):
    email: str  # Match your CSV column name

# Classification route
@app.post("/classify_email/")
def classify_email_api(input_data: EmailInput):
    original_email = input_data.email
    
    # Mask PII
    masked_text, masked_entities = mask_pii(original_email)

    # Predict category
    vectorized = vectorizer.transform([masked_text])
    predicted_category = model.predict(vectorized)[0]

    return {
        "input_email_body": original_email,
        "list_of_masked_entities": masked_entities,
        "masked_email": masked_text,
        "category_of_the_email": predicted_category
    }

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import joblib
# from utils import mask_pii
# import joblib

# vectorizer = joblib.load("saved_models/vectorizer.joblib")
# model = joblib.load("saved_models/model.joblib")

# print("✅ Vectorizer and model loaded successfully!")

# app = FastAPI()
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Email Classification API!"}

# import os

# vectorizer_path = "saved_models/vectorizer.joblib"
# if not os.path.exists(vectorizer_path):
#     raise FileNotFoundError(f"Vectorizer file not found at: {vectorizer_path}")
# else:
#     print("Vectorizer file found! Proceeding to load...")

# import joblib
# vectorizer = joblib.load(vectorizer_path)

# vectorizer = joblib.load("saved_models/vectorizer.joblib")
# model = joblib.load("saved_models/model.joblib")

# class EmailInput(BaseModel):
#     input_email_body: str

# @app.post("/")
# def classify_email(input_data: EmailInput):
#     original_email = input_data.input_email_body
#     masked_text, masked_entities = mask_pii(original_email)

#     vectorized = vectorizer.transform([masked_text])
#     category = model.predict(vectorized)[0]

#     return {
#         "input_email_body": original_email,
#         "list_of_masked_entities": masked_entities,
#         "masked_email": masked_text,
#         "category_of_the_email": category
#     }
