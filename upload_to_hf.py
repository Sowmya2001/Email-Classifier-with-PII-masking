from huggingface_hub import upload_file

repo_id = "Sowmya-19/email-classifier-api"

files_to_upload = files_to_upload = [
    ("app.py", "app.py"),
    ("requirements.txt", "requirements.txt"),
    ("Dockerfile", "Dockerfile"),
    ("emails.csv", "emails.csv")  # if this is <10MB or LFS tracked
]


for local_path, remote_path in files_to_upload:
    upload_file(
        path_or_fileobj=local_path,
        path_in_repo=remote_path,
        repo_id=repo_id,
        repo_type="space"
    )
    print(f"✅ Uploaded: {local_path} ➝ {remote_path}")

