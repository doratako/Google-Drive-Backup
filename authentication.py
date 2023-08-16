import os.path
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate(scope):
    creds = None

    if os.path.exists("service_account_key.json"):
        creds = service_account.Credentials.from_service_account_file('service_account_key.json', scopes=scope)
        return creds
    
def create_service(auth):
    try:
        service = build('drive', 'v3', credentials=auth)

    except HttpError as error:
        print(f'An error occurred: {error}')

    return service


creds = authenticate(SCOPES)
drive_service = create_service(creds)  # returns drive Resource object
