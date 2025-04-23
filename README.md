---
title: Email Classifier Api
emoji: 📚
colorFrom: gray
colorTo: blue
sdk: docker
pinned: false
license: apache-2.0
---
# 📧 Email Classifier with PII Masking

A FastAPI-based project that classifies emails into categories and masks Personally Identifiable Information (PII) from the email content. Deployed on Hugging Face Spaces and integrated with GitHub.

---

## 🚀 Features

- ✅ Classifies emails into predefined categories
- 🔒 Masks sensitive PII information (emails, phone numbers, etc.)
- 🔎 RESTful API built with **FastAPI**
- 💻 Interactive Swagger UI available at `/docs`
- 🧠 Machine Learning model trained from scratch using Scikit-learn
- ☁️ Hugging Face Spaces deployment support
- 🐘 Git Large File Storage (LFS) for model files
- 🔁 GitHub integration with version control

---

## 🧠 Modules Used

- `FastAPI`, `pydantic`, `uvicorn` – for API
- `sklearn`, `joblib`, `pandas` – for ML model & preprocessing
- `re`, `os`, `typing`, `json` – for data handling and regex-based PII masking

---
## 📂 Project Structure

├── api.py # FastAPI application with endpoints 
├── models.py # ML model loading & classification 
├── utils.py # PII masking and helper functions 
├── data_explore.py # Data cleaning and preparation 
├── vectorizer.joblib/
├── model.joblib/
├── email_classifier_model.joblib/# Trained models (tracked via Git LFS) 
├── emails.csv # Sample dataset (LFS tracked) 
├── README.md # This file

---

## ⚙️ Setup & Run Locally

```bash
# Clone the repository
git clone https://github.com/Sowmya2001/Email-Classifier-with-PII-masking
cd Email-Classifier-with-PII-masking

# Install dependencies
pip install -r requirements.txt

# Option 1: Run FastAPI server with Swagger UI
uvicorn api:app --reload

# Option 2: Run FastAPI + Gradio server
uvicorn app:app --reload
```
Navigate to http://127.0.0.1:8000/docs to access the Swagger UI.
check out the Swagger UI api post url : http://127.0.0.1:8000/classify_email/
Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
check out the Gradio interface url :  https://sowmya-19-email-classifier-api.hf.space/
check out the Postman api post url : http://127.0.0.1:8000/api/classify 

![Screenshot 2025-04-23 121246](https://github.com/user-attachments/assets/48056444-8906-4bcc-b498-b11afa79f469)  Gradio Interface
![Screenshot 2025-04-23 112929](https://github.com/user-attachments/assets/0231b752-a0d6-480d-bddc-defdb3781958)  Postman API
![Screenshot 2025-04-23 122054](https://github.com/user-attachments/assets/a7826b7e-1199-41a3-9cab-970728200e41)  Swagger API
