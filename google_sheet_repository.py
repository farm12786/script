from __future__ import print_function

import os.path
import gspread


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from requests import request


class GoogleSheetRepository:
    def __init__(self, sheet_title: str = None) -> None:
        self.sheet_title = sheet_title
        self.sh = None
        self.SCOPES = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]
        self.creds = None
        self.service = None
        self.gc = None
        # self.__config_credential()
        # self.__set_service()
        self.__set_gc()
        if sheet_title:
            self.__set_sh()

    def __config_credential(self):
        if os.path.exists("./credential/token.json"):
            self.creds = Credentials.from_authorized_user_file(
                "./credential/token.json", self.SCOPES
            )
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "./credential/credentials.json", self.SCOPES
                )
                self.creds = flow.run_local_server(port=53238)
            with open("./credential/token.json", "w") as token:
                token.write(self.creds.to_json())

    def __set_service(self):
        self.service = build("sheets", "v4", credentials=self.creds)

    def __set_gc(self):
        self.gc = gspread.oauth(
            credentials_filename="./credential/desktop_app_credential.json",
            authorized_user_filename="./credential/token.json",
            client_factory=gspread.BackoffClient
        )

    def __set_sh(self):
        self.sh = self.gc.open(self.sheet_title)

    def create_sheet(self, title: str):
        self.gc.create(title)

    def add_worksheet(self, worksheet_title: str, rows: int = 1000, cols: int = 26):
        worksheet = self.sh.add_worksheet(title=worksheet_title, rows=rows, cols=cols)
        print(f"worksheet '{worksheet_title}' : created")

    def delete_worksheet(self, worksheet):
        self.sh.del_worksheet(worksheet)
        print(f"worksheet '{worksheet.title}' : deleted")

    def get_worksheets(self):
        worksheet_list = self.sh.worksheets()
        return worksheet_list

    def get_worksheet_by_title(self, worksheet_title: str):
        try:
            worksheet = self.sh.worksheet(worksheet_title)
            return worksheet
        except gspread.exceptions.WorksheetNotFound:
            return False

    def update_worksheet(
        self, worksheet_title: str, column_list: list, data_list: list
    ):
        worksheet = self.sh.worksheet(worksheet_title)
        worksheet.update(column_list + data_list)

    def worksheet_formatting(self, worksheet_title: str, cell_range: str, format: dict):
        worksheet = self.sh.worksheet(worksheet_title)
        worksheet.format(cell_range, format)
        print(f"worksheet '{worksheet.title}' : formatted")
