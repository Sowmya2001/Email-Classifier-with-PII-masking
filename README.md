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
Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
check out the Gradio interface url :  https://sowmya-19-email-classifier-api.hf.space/
check out the api post url : http://127.0.0.1:8000/api/classify via Postman
