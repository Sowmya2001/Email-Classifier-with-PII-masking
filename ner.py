# ner.py
from transformers import pipeline

# Load a Hugging Face transformer-based pipeline for NLP tasks
nlp = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

# Example text for NER
result = nlp("Hugging Face is creating a tool that democratizes AI.")
print(result)
