# from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleSheetRepository:
    def __init__(self) -> None:
        self.SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        self.creds = None

    def config_credential(self):
        if os.path.exists("token.json"):
            self.creds = Credentials.from_authorized_user_file(
                "token.json", self.SCOPES
            )
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "./credential/credentials.json", self.SCOPES
                )
                self.creds = flow.run_local_server(port=53238)
            # Save the credentials for the next run
            with open("./credential/token.json", "w") as token:
                token.write(self.creds.to_json())
                
