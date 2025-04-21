import re

PII_ENTITIES = {
    "full_name": r'\b([A-Z][a-z]+ [A-Z][a-z]+)\b',
    "email": r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b',
    "phone_number": r'\b(?:\+91[-\s]?|0)?[6-9]\d{9}\b',
    "dob": r'\b\d{2}[/-]\d{2}[/-]\d{4}\b',
    "aadhar_num": r'\b\d{4} \d{4} \d{4}\b',
    "credit_debit_no": r'\b(?:\d{4}[- ]?){3}\d{4}\b',
    "cvv_no": r'\b\d{3}\b',
    "expiry_no": r'\b(0[1-9]|1[0-2])\/\d{2,4}\b',
}

def mask_pii(text):
    masked_text = text
    masked_entities = []

    for label, pattern in PII_ENTITIES.items():
        for match in re.finditer(pattern, masked_text):
            start, end = match.span()
            original = match.group()
            masked_text = masked_text.replace(original, f"[{label}]")
            masked_entities.append({
                "position": [start, end],
                "classification": label,
                "entity": original
            })

    return masked_text, masked_entities

