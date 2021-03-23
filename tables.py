from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
from enum import Enum


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'
SAMPLE_SPREADSHEET_ID = '1Frcbgjv5cHeauL8ZFzVCpVRFkEqevaTu0qEhhqY8bck'

BACHELOR_RANGE = "bachelor!A1:A1000"
MASTER_RANGE = "master!A1:A1000"

credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()


class UserType(Enum):
    BACHELOR = "BACHELOR"
    MASTER = "MASTER"


def add_to_table(chat_id, name, faculty, phone):
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=BACHELOR_RANGE).execute()
    values = result.get('values', [])

    for value in values:
        if str(chat_id) == str(value[0]):
            return False

    data = [[chat_id, name, faculty, phone, "false"]]
    request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=BACHELOR_RANGE,
                                    valueInputOption="USER_ENTERED",
                                    insertDataOption='INSERT_ROWS',
                                    body={"values": data}).execute()
    return True


def check_in_queue(chat_id):
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="bachelor!A1:E1000").execute()
    values = result.get('values', [])
    print(values)

    i = 0
    for value in values:
        if str(chat_id) != str(value[0]) and str(value[4]) == "FALSE":
            i += 1
        elif str(chat_id) == str(value[0]) and str(value[4] == "FALSE"):
            i += 1
            return i

    return -1



