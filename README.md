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

Swagger UI api post method url : http://127.0.0.1:8000/classify_email/ (This link is just used to know the url of our api endpoint in Swagger UI page after test the post method)

Main Hugging Face Url : https://huggingface.co/spaces/Sowmya-19/email-classifier-api/tree/main

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

check out the Gradio interface url :  https://sowmya-19-email-classifier-api.hf.space/

To test the Postman api post method url : http://127.0.0.1:8000/api/classify (Paste this url in Postman website(Download the postman desktop agent through website: https://web.postman.co/workspace/c360a277-8cfc-4d3a-8e82-a5310b60bf00/request/create?requestId=cb8e8ebf-782d-485a-9f21-a82cbc4c4c42) by selecting post method and give the raw data under body by selecting the JSON in dropdown).

Postman API  ![Screenshot 2025-04-23 121246](https://github.com/user-attachments/assets/48056444-8906-4bcc-b498-b11afa79f469) 

Gradio Interface  ![Screenshot 2025-04-23 112929](https://github.com/user-attachments/assets/0231b752-a0d6-480d-bddc-defdb3781958)  

Swagger API  ![Screenshot 2025-04-23 122109](https://github.com/user-attachments/assets/6f854023-2f88-4ae8-b355-ab9648c5c971)
