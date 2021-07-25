from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
from enum import Enum


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'
SAMPLE_SPREADSHEET_ID_BUDGET = '1jsgV24aj54nxVcbkaNTyF6Nu2vV_eGDIFdf2skjI7mU'
SAMPLE_SPREADSHEET_ID_CONTRACT = '1viJe4xpl8NsLXUfK5g8DOphP5xFeF6vIw30nr-Sni04'

BACHELOR_RANGE = "Bachelor_budget!A1:Y1000"
MASTER_RANGE = "master!A1:У1000"

credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()


class UserType(Enum):
    BACHELOR = "BACHELOR"
    MASTER = "MASTER"


# def add_to_table(chat_id, name, faculty, phone):
#     result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=BACHELOR_RANGE).execute()
#     values = result.get('values', [])
#
#     for value in values:
#         if str(chat_id) == str(value[0]):
#             return False
#
#     data = [[chat_id, name, faculty, phone, "false"]]
#     request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                     range=BACHELOR_RANGE,
#                                     valueInputOption="USER_ENTERED",
#                                     insertDataOption='INSERT_ROWS',
#                                     body={"values": data}).execute()
#     return True


def check_in_queue(user_name):
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_BUDGET, range=BACHELOR_RANGE).execute()
    values = result.get('values', [])

    i = 0
    user_name = str(user_name)
    for value in values:
        name = str(value[1])
        if user_name != name:
            i += 1
        elif user_name == name:
            return i

    return -1



