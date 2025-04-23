from huggingface_hub import upload_file

# Define the repository ID where you want to upload the models
repo_id = "Sowmya-19/email-classifier-api"  # Replace with your own repository name

# List of files to upload along with their remote paths
files_to_upload = [
    ("saved_models/email_classifier_model.joblib", "email_classifier_model.joblib"),
    ("saved_models/vectorizer.joblib", "vectorizer.joblib"),
    ("saved_models/model.joblib", "model.joblib")
]

# Loop through the files and upload them to the Hugging Face Space
for local_path, remote_path in files_to_upload:
    upload_file(
        path_or_fileobj=local_path,
        path_in_repo=remote_path,
        repo_id=repo_id,
        repo_type="space"
    )
    print(f"✅ Uploaded: {local_path} ➝ {remote_path}")
