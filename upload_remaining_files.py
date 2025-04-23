from huggingface_hub import upload_file

repo_id = "Sowmya-19/email-classifier-api"

files_to_upload = [
    # ("models.py", "models.py"),
    # ("utils.py", "utils.py"),
    # ("data_explore.py", "data_explore.py"),
    # ("train_model.py", "train_model.py"),
    # ("api.py", "api.py")
    # ("gradio_ui.py", "gradio_ui.py")
    # ("install.sh", "install.sh")
    # ("ner.py", "ner.py")
    (".env", ".env")
]

for local_path, remote_path in files_to_upload:
    upload_file(
        path_or_fileobj=local_path,
        path_in_repo=remote_path,
        repo_id=repo_id,
        repo_type="space"
    )
    print(f"✅ Uploaded: {local_path} ➝ {remote_path}")
