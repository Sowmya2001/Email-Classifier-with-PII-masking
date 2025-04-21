from fastapi import FastAPI
from pydantic import BaseModel
from utils import mask_pii
from models import classify_email

app = FastAPI()

class EmailRequest(BaseModel):
    email: str

class MaskedEntity(BaseModel):
    position: list
    classification: str
    entity: str

@app.post("/classify_email/")
async def classify_email_api(request: EmailRequest):
    email = request.email
    
    # Mask PII from the email
    masked_email, masked_entities = mask_pii(email)
    
    # Classify the email
    category = classify_email(masked_email)
    
    # Prepare the response
    return {
        "input_email_body": email,
        "list_of_masked_entities": masked_entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }




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
