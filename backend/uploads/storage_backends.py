import os, io, json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaIoBaseUpload
from django.conf import settings
from .helper import update_env_var
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


# creating tmp directory for runtime in different os. 
TMP_DIR = os.environ.get("TMPDIR") or os.environ.get("TEMP") or "/tmp"
APP_TMP = os.path.join(TMP_DIR, "localjobhunt_drive")
os.makedirs(APP_TMP, exist_ok=True)

#creating token/creds path and joining with the temp folder created. 
TOKEN_PATH = os.path.join(APP_TMP, "token.json")
CREDENTIALS_PATH = os.path.join(APP_TMP, "credentials.json")

# filling up the credentials.json and token.json with the data from .env
if "GOOGLE_CREDENTIALS" in os.environ:
    creds_json = json.loads(settings.GOOGLE_CREDENTIALS)
    with open(CREDENTIALS_PATH, "w") as f:
        f.write(json.dumps(creds_json))

if "GOOGLE_TOKEN" in os.environ:
    token_json = json.loads(settings.GOOGLE_TOKEN) 
    with open(TOKEN_PATH, "w") as f:
        f.write(json.dumps(token_json))

SCOPES = ['https://www.googleapis.com/auth/drive']

# Cache the service instance to avoid rebuilding
_drive_service = None

def get_drive_service():
    global _drive_service
    
    # Return cached service if available
    if _drive_service is not None:
        return _drive_service
    
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        # Update token file after refresh
        with open(TOKEN_PATH, 'w') as token_file:
            token_file.write(creds.to_json())

    if not creds or not creds.valid:
        raise Exception("Invalid Google token. Cannot do OAuth on Render.")

    _drive_service = build('drive', 'v3', credentials=creds)
    return _drive_service

def drive_upload(file, folder_id):
    service = get_drive_service()

    file_metadata = {
        'name': file.name,
        'parents': [folder_id]  
    }

    # Use chunked upload with resumable=True for large files
    # This prevents loading the entire file into memory at once
    media = MediaIoBaseUpload(
        file, 
        mimetype=file.content_type,
        chunksize=1024*1024,  # 1MB chunks
        resumable=True
    )

    uploaded = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id, webViewLink'
    ).execute()

    service.permissions().create(
        fileId=uploaded['id'],
        body={'role': 'reader', 'type': 'anyone'}
    ).execute()

    # Clear the file from memory
    file.seek(0)  # Reset file pointer if needed elsewhere
    
    return f"https://drive.google.com/uc?export=view&id={uploaded['id']}"