from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = '../../../Desktop/New folder (4)/keys.json'
SAMPLE_SPREADSHEET_ID = '1Frcbgjv5cHeauL8ZFzVCpVRFkEqevaTu0qEhhqY8bck'

credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()


def add_to_table(chat_id, name, faculty, phone):
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="test2!A1:A100").execute()
    values = result.get('values', [])

    for value in values:
        if str(chat_id) == str(value[0]):
            return False

    data = [[chat_id, name, faculty, phone, "false"]]
    request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="test2!A1",
                                    valueInputOption="USER_ENTERED",
                                    insertDataOption='INSERT_ROWS',
                                    body={"values": data}).execute()
    return True


def check_in_queue(chat_id):
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="test2!A1:E100").execute()
    values = result.get('values', [])

    i = 0
    for value in values:
        if str(chat_id) != str(value[0]) and str(value[4]) == "FALSE":
            i += 1
        elif str(chat_id) == str(value[0]) and str(value[4] == "FALSE"):
            i += 1
            return i

    return -1


