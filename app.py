# import gradio as gr
# from fastapi import FastAPI
# from pydantic import BaseModel
# from utils import mask_pii
# from models import classify_email
# from models import predict 

# # Create FastAPI app
# app = FastAPI()

# class EmailRequest(BaseModel):
#     email: str

# class MaskedEntity(BaseModel):
#     position: list
#     classification: str
#     entity: str

# # Define API endpoint
# @app.post("/classify_email/")
# async def classify_email_api(request: EmailRequest):
#     email = request.email
    
#     # Mask PII from the email
#     masked_email, masked_entities = mask_pii(email)
    
#     # Classify the email
#     category = classify_email(masked_email)
    
#     return {
#         "input_email_body": email,
#         "list_of_masked_entities": masked_entities,
#         "masked_email": masked_email,
#         "category_of_the_email": category
#     }

# # Create Gradio interface for the FastAPI app
# def classify_email_gradio(email):
#     return classify_email_api(EmailRequest(email=email))

# # Gradio interface for FastAPI route
# gr.Interface(fn=classify_email_gradio, inputs="text", outputs="json").launch(server_name="0.0.0.0", server_port=5000)


# import gradio as gr
# import joblib
# from utils import mask_pii
# import os
# import tempfile
# import warnings

# # 1. Configure environment
# warnings.filterwarnings("ignore")

# # 2. Set up directories
# try:
#     temp_dir = tempfile.gettempdir()
#     os.environ["MPLCONFIGDIR"] = temp_dir
#     print(f"✅ Using temp directory: {temp_dir}")
# except Exception as e:
#     print(f"⚠️ Directory warning: {str(e)}")

# # 3. Load models
# try:
#     vectorizer = joblib.load("vectorizer.joblib")
#     model = joblib.load("model.joblib")
#     print("✅ Models loaded successfully")
# except Exception as e:
#     raise RuntimeError(f"❌ Model loading failed: {str(e)}")

# # 4. Classification function
# def classify_email(email_text):
#     try:
#         masked_text, masked_entities = mask_pii(email_text)
#         vectorized = vectorizer.transform([masked_text])
#         predicted_category = model.predict(vectorized)[0]
#         return (
#             email_text,
#             masked_text,
#             str(masked_entities),
#             predicted_category
#         )
#     except Exception as e:
#         return (
#             f"Error: {str(e)}",
#             "",
#             "",
#             "Error"
#         )

# # 5. Create Gradio interface
# iface = gr.Interface(
#     fn=classify_email,
#     inputs=gr.Textbox(
#         lines=10,
#         label="Enter Email Text",
#         placeholder="Paste email content here..."
#     ),
#     outputs=[
#         gr.Textbox(label="Original Email"),
#         gr.Textbox(label="Masked Email"),
#         gr.Textbox(label="Masked Entities"),
#         gr.Textbox(label="Email Category")
#     ],
#     title="📧 Email Classifier with PII Masking",
#     description="This tool classifies emails while automatically masking personal information.",
#     allow_flagging="never",
#     examples=[
#         ["Subject: Urgent - System Failure\nOur production server crashed..."],
#         ["Hello, please reset my password for account johndoe@example.com"]
#     ]
# )

# # 6. Create ASGI app for Uvicorn
# app = iface.app

# # 7. Launch logic
# if __name__ == "__main__":
#     iface.launch(
#         server_name="127.0.0.1",
#         server_port=7860,
#         show_error=True
#     )

# from fastapi import FastAPI, Request
# from pydantic import BaseModel
# from gradio.routes import mount_gradio_app
# import gradio as gr
# import joblib
# from utils import mask_pii
# import os
# import tempfile
# import warnings

# # ========== Environment & Setup ==========
# warnings.filterwarnings("ignore")
# temp_dir = tempfile.gettempdir()
# os.environ["MPLCONFIGDIR"] = temp_dir
# print(f"✅ Using temp directory: {temp_dir}")

# # ========== Load Models ==========
# try:
#     vectorizer = joblib.load("vectorizer.joblib")
#     model = joblib.load("model.joblib")
#     print("✅ Models loaded successfully")
# except Exception as e:
#     raise RuntimeError(f"❌ Model loading failed: {str(e)}")

# # ========== Classification Logic ==========
# def classify_text(email_text: str):
#     masked_text, masked_entities = mask_pii(email_text)
#     vectorized = vectorizer.transform([masked_text])
#     predicted_category = model.predict(vectorized)[0]
#     return {
#         "original_email": email_text,
#         "masked_email": masked_text,
#         "masked_entities": str(masked_entities),
#         "predicted_category": predicted_category
#     }

# # ========== FastAPI App ==========
# app = FastAPI()

# # ========== POST API Endpoint ==========
# class EmailRequest(BaseModel):
#     text: str

# @app.post("/api/classify")
# def classify_api(data: EmailRequest):
#     return classify_text(data.text)

# # ========== Gradio UI ==========
# gr_interface = gr.Interface(
#     fn=lambda text: list(classify_text(text).values()),
#     inputs=gr.Textbox(
#         lines=10,
#         label="Enter Email Text",
#         placeholder="Paste email content here..."
#     ),
#     outputs=[
#         gr.Textbox(label="Original Email"),
#         gr.Textbox(label="Masked Email"),
#         gr.Textbox(label="Masked Entities"),
#         gr.Textbox(label="Email Category")
#     ],
#     title="📧 Email Classifier with PII Masking",
#     description="This tool classifies emails while automatically masking personal information.",
#     allow_flagging="never",
#     examples=[
#         ["Subject: Urgent - System Failure\nOur production server crashed..."],
#         ["Hello, please reset my password for account johndoe@example.com"]
#     ]
# )

# # Mount Gradio at /gradio
# app = mount_gradio_app(app, gr_interface, path="/gradio")

# # ========== Run this using Uvicorn ==========
# # Example command:
# # uvicorn app:app --host 127.0.0.1 --port 7880 --reload


# import gradio as gr
# import joblib
# from utils import mask_pii
# import os
# import tempfile
# import warnings
# from fastapi import FastAPI, Request, HTTPException
# from fastapi.responses import JSONResponse

# # 1. Configure environment
# warnings.filterwarnings("ignore")
# os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib"

# # 2. Load models
# try:
#     vectorizer = joblib.load("vectorizer.joblib")
#     model = joblib.load("model.joblib")
#     print("✅ Models loaded successfully")
# except Exception as e:
#     raise RuntimeError(f"❌ Model loading failed: {str(e)}")

# # 3. Classification function
# def classify_email(email_text):
#     try:
#         masked_text, masked_entities = mask_pii(email_text)
#         vectorized = vectorizer.transform([masked_text])
#         predicted_category = model.predict(vectorized)[0]
#         return (
#             email_text,
#             masked_text,
#             str(masked_entities),
#             predicted_category
#         )
#     except Exception as e:
#         return (
#             f"Error: {str(e)}",
#             "",
#             "",
#             "Error"
#         )

# # 4. Create FastAPI app
# app = FastAPI()

# # 5. Add custom API endpoint
# @app.post("/api/classify")
# async def api_classify(request: Request):
#     try:
#         data = await request.json()
#         email = data.get("email", "").strip()
#         if not email:
#             raise HTTPException(status_code=400, detail="Email is required")
        
#         original, masked, entities, category = classify_email(email)
#         return {
#             "original_text": original,
#             "masked_text": masked,
#             "entities": entities,
#             "category": category
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # 6. Gradio interface function
# def gradio_wrapper(email_text: str):
#     return classify_email(email_text)

# # 7. Create Gradio interface
# iface = gr.Interface(
#     fn=gradio_wrapper,
#     inputs=gr.Textbox(
#         lines=10,
#         label="Enter Email Text",
#         placeholder="Paste email content here..."
#     ),
#     outputs=[
#         gr.Textbox(label="Original Email"),
#         gr.Textbox(label="Masked Email"),
#         gr.Textbox(label="Masked Entities"),
#         gr.Textbox(label="Email Category")
#     ],
#     title="📧 Email Classifier with PII Masking",
#     description="This tool classifies emails while automatically masking personal information.",
#     allow_flagging="never",
#     examples=[
#         ["Subject: Urgent - System Failure\nOur production server crashed..."],
#         ["Hello, please reset my password for account johndoe@example.com"]
#     ]
# )

# # 8. Mount Gradio app
# app = gr.mount_gradio_app(app, iface, path="/gradio")

# # 9. Launch configuration
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(
#         app,
#         host="127.0.0.1",
#         port=7880,
#         log_level="info"
#     )

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
    text: str

# API endpoint
@app.post("/api/classify")
def classify_api(request: EmailRequest):
    return classify_email(request.text)

# Mount Gradio at root
app = mount_gradio_app(app, gr_interface, path="/")


# from fastapi import FastAPI
# from pydantic import BaseModel
# import gradio as gr
# import joblib
# from utils import mask_pii
# import os
# import tempfile
# import warnings
# from gradio.routes import mount_gradio_app

# # Configure environment
# warnings.filterwarnings("ignore")
# temp_dir = tempfile.gettempdir()
# os.environ["MPLCONFIGDIR"] = temp_dir
# print(f"✅ Using temp directory: {temp_dir}")

# # Load models
# try:
#     vectorizer = joblib.load("vectorizer.joblib")
#     model = joblib.load("model.joblib")
#     print("✅ Models loaded successfully")
# except Exception as e:
#     raise RuntimeError(f"❌ Model loading failed: {str(e)}")

# # Classification logic
# def classify_email(email_text):
#     try:
#         masked_text, masked_entities = mask_pii(email_text)
#         vectorized = vectorizer.transform([masked_text])
#         predicted_category = model.predict(vectorized)[0]
#         return {
#         "input_email_body": email_text,
#         "list_of_masked_entities": masked_entities,
#         "masked_email": masked_text,
#         "category_of_the_email": predicted_category
#     }
#     except Exception as e:
#         return (
#             f"Error: {str(e)}",
#             "",
#             "",
#             "Error"
#         )

# # Gradio interface
# gr_interface = gr.Interface(
#     fn=classify_email,
#     inputs=gr.Textbox(lines=10, label="Enter Email Text"),
#     outputs=[
#         gr.Textbox(label="Original Email"),
#         gr.Textbox(label="Masked Email"),
#         gr.Textbox(label="Masked Entities"),
#         gr.Textbox(label="Email Category")
#     ],
#     title="📧 Email Classifier with PII Masking",
#     description="This tool classifies emails while masking personal information.",
#     allow_flagging="never"
# )

# # FastAPI setup
# app = FastAPI()

# # API model for POST request
# class EmailRequest(BaseModel):
#     text: str

# # API endpoint
# # @app.post("/classify_email/")
# # def classify_email_api(input_data: EmailInput):
# #     original_email = input_data.email
    
# #     # Mask PII
# #     masked_text, masked_entities = mask_pii(original_email)

# #     # Predict category
# #     vectorized = vectorizer.transform([masked_text])
# #     predicted_category = model.predict(vectorized)[0]

# #     return {
# #         "input_email_body": original_email,
# #         "list_of_masked_entities": masked_entities,
# #         "masked_email": masked_text,
# #         "category_of_the_email": predicted_category
# #     }
# @app.post("/api/classify")
# def classify_api(request: EmailRequest):
#     result = classify_email(request.text)
#     return {
#         "input_email_body": result[0],
#         "list_of_masked_entities": result[1],
#         "masked_email": result[2],
#         "category_of_the_email": result[3]
#     }


# # Mount Gradio at root (or change to "/gradio")
# app = mount_gradio_app(app, gr_interface, path="/")

# # To run: uvicorn app:app --host 127.0.0.1 --port 7880 --reload


# import gradio as gr
# import joblib
# from utils import mask_pii
# import os
# import tempfile
# import warnings

# # 1. Configure environment
# warnings.filterwarnings("ignore")

# # 2. Set up directories
# try:
#     temp_dir = tempfile.gettempdir()
#     os.environ["MPLCONFIGDIR"] = temp_dir
#     print(f"✅ Using temp directory: {temp_dir}")
# except Exception as e:
#     print(f"⚠️ Directory warning: {str(e)}")

# # 3. Load models
# try:
#     vectorizer = joblib.load("vectorizer.joblib")
#     model = joblib.load("model.joblib")
#     print("✅ Models loaded successfully")
# except Exception as e:
#     raise RuntimeError(f"❌ Model loading failed: {str(e)}")

# # 4. Classification function
# def classify_email(email_text):
#     try:
#         masked_text, masked_entities = mask_pii(email_text)
#         vectorized = vectorizer.transform([masked_text])
#         predicted_category = model.predict(vectorized)[0]
#         return (
#             email_text,
#             masked_text,
#             str(masked_entities),
#             predicted_category
#         )
#     except Exception as e:
#         return (
#             f"Error: {str(e)}",
#             "",
#             "",
#             "Error"
#         )

# # 5. Create Gradio interface
# iface = gr.Interface(
#     fn=classify_email,
#     inputs=gr.Textbox(
#         lines=10,
#         label="Enter Email Text",
#         placeholder="Paste email content here..."
#     ),
#     outputs=[
#         gr.Textbox(label="Original Email"),
#         gr.Textbox(label="Masked Email"),
#         gr.Textbox(label="Masked Entities"),
#         gr.Textbox(label="Email Category")
#     ],
#     title="📧 Email Classifier with PII Masking",
#     description="This tool classifies emails while automatically masking personal information.",
#     allow_flagging="never",
#     examples=[
#         ["Subject: Urgent - System Failure\nOur production server crashed..."],
#         ["Hello, please reset my password for account johndoe@example.com"]
#     ]
# )


# # 6. Create ASGI app for Uvicorn
# app = iface.app


# # 7. Launch logic
# if __name__ == "__main__":
#     iface.launch(
#         server_name="127.0.0.1",
#         server_port=7880,
#         show_error=True
#     )

# from fastapi import FastAPI
# from pydantic import BaseModel
# from utils import mask_pii
# from models import classify_email

# app = FastAPI()

# class EmailRequest(BaseModel):
#     email: str

# class MaskedEntity(BaseModel):
#     position: list
#     classification: str
#     entity: str

# @app.post("/classify_email/")
# async def classify_email_api(request: EmailRequest):
#     email = request.email
    
#     # Mask PII from the email
#     masked_email, masked_entities = mask_pii(email)
    
#     # Classify the email
#     category = classify_email(masked_email)
    
#     # Prepare the response
#     return {
#         "input_email_body": email,
#         "list_of_masked_entities": masked_entities,
#         "masked_email": masked_email,
#         "category_of_the_email": category
#     }




# {
#  "cells": [
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "id": "2af9eb58",
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "!pip install fastapi\n",
#     "from fastapi import FastAPI, HTTPException\n",
#     "from pydantic import BaseModel\n",
#     "from utils import mask_pii\n",
#     "from models import classify_email\n",
#     "\n",
#     "app = FastAPI()\n",
#     "\n",
#     "class EmailRequest(BaseModel):\n",
#     "    email_body: str\n",
#     "\n",
#     "@app.post(\"/predict\")\n",
#     "def predict_email_category(payload: EmailRequest):\n",
#     "    original_text = payload.email_body\n",
#     "    masked_text, entities = mask_pii(original_text)\n",
#     "    category = classify_email(masked_text)\n",
#     "\n",
#     "    return {\n",
#     "        \"input_email_body\": original_text,\n",
#     "        \"list_of_masked_entities\": entities,\n",
#     "        \"masked_email\": masked_text,\n",
#     "        \"category_of_the_email\": category\n",
#     "    }\n"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "id": "e2055566",
#    "metadata": {},
#    "outputs": [],
#    "source": []
#   }
#  ],
#  "metadata": {
#   "kernelspec": {
#    "display_name": "Python 3 (ipykernel)",
#    "language": "python",
#    "name": "python3"
#   },
#   "language_info": {
#    "codemirror_mode": {
#     "name": "ipython",
#     "version": 3
#    },
#    "file_extension": ".py",
#    "mimetype": "text/x-python",
#    "name": "python",
#    "nbconvert_exporter": "python",
#    "pygments_lexer": "ipython3",
#    "version": "3.9.12"
#   }
#  },
#  "nbformat": 4,
#  "nbformat_minor": 5
# }
