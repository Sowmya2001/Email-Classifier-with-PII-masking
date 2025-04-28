
from fastapi import FastAPI
from pydantic import BaseModel
import gradio as gr
import joblib
from utils import mask_pii
import os
import tempfile
import warnings
from gradio.routes import mount_gradio_app

# Configure environment
warnings.filterwarnings("ignore")
temp_dir = tempfile.gettempdir()
os.environ["MPLCONFIGDIR"] = temp_dir
print(f"✅ Using temp directory: {temp_dir}")

# Load models
try:
    vectorizer = joblib.load("vectorizer.joblib")
    model = joblib.load("model.joblib")
    print("✅ Models loaded successfully")
except Exception as e:
    raise RuntimeError(f"❌ Model loading failed: {str(e)}")

# Classification logic
def classify_email(email_text):
    try:
        masked_text, masked_entities = mask_pii(email_text)
        vectorized = vectorizer.transform([masked_text])
        predicted_category = model.predict(vectorized)[0]
        return {
            "input_email_body": email_text,
            "list_of_masked_entities": masked_entities,
            "masked_email": masked_text,
            "category_of_the_email": predicted_category
        }
    except Exception as e:
        return {
            "error": str(e),
            "input_email_body": "",
            "list_of_masked_entities": "",
            "masked_email": "",
            "category_of_the_email": "Error"
        }

# Gradio interface
gr_interface = gr.Interface(
    fn=lambda x: [
        x,
        classify_email(x)["masked_email"],
        str(classify_email(x)["list_of_masked_entities"]),
        classify_email(x)["category_of_the_email"]
    ],
    inputs=gr.Textbox(lines=10, label="Enter Email Text"),
    outputs=[
        gr.Textbox(label="Original Email"),
        gr.Textbox(label="Masked Email"),
        gr.Textbox(label="Masked Entities"),
        gr.Textbox(label="Email Category")
    ],
    title="📧 Email Classifier with PII Masking",
    description="This tool classifies emails while masking personal information.",
    allow_flagging="never"
)

# FastAPI setup
app = FastAPI()

# API model for POST request
class EmailRequest(BaseModel):
    email: str

# API endpoint
@app.post("/api/classify")
def classify_api(request: EmailRequest):
    return classify_email(request.email)

# Mount Gradio at root
app = mount_gradio_app(app, gr_interface, path="/")

# To run use uvicorn app:app -reload


