from src.config_loader import load_config

from google.oauth2 import service_account
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "service_account.json"

config =  load_config('config/sheet_config.yml')
SPREADSHEET_ID =config['spreadsheetId']
SHEET_NAME = config['sheetName']


def get_sheets_service():
	credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES,
    )
	service = build("sheets", "v4", credentials=credentials)
	return service


def clear_raw_data():
	service = get_sheets_service()
	sheet_values = service.spreadsheets().values()

	sheet_values.clear(
        spreadsheetId=SPREADSHEET_ID,
        range=f"{SHEET_NAME}!A1:Z10000",
        body={}
    ).execute()


def write_raw_data(rows: list[list[str]]):
	service = get_sheets_service()
	sheet_values = service.spreadsheets().values()

	body = {"values": rows}

	result = sheet_values.update(
        spreadsheetId=SPREADSHEET_ID,
        range=f"{SHEET_NAME}!A1",
        valueInputOption="RAW",
        body=body,
    ).execute()

	print(f"Updated cells: {result.get('updatedCells')}")
