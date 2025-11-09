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

def get_drive_service():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())


    # if not creds or not creds.valid:
    #     flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
    #     creds = flow.run_local_server(port=0)
    #     with open(TOKEN_PATH, 'w') as token_file:
    #         token_file.write(creds.to_json())
    #     update_env_var("GOOGLE_TOKEN", json.loads(creds.to_json()))
    
    
    if not creds or not creds.valid:
        raise Exception("Invalid Google token. Cannot do OAuth on Render.")

    service = build('drive', 'v3', credentials=creds)
    return service

def drive_upload(file, folder_id):
    service = get_drive_service()

    file_metadata = {
        'name': file.name,
        'parents': [folder_id]  
    }

    media = MediaIoBaseUpload(file, mimetype=file.content_type)


    uploaded = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id, webViewLink'
    ).execute()

    service.permissions().create(
        fileId=uploaded['id'],
        body={'role': 'reader', 'type': 'anyone'}
    ).execute()

    return f"https://drive.google.com/uc?export=view&id={uploaded['id']}"
