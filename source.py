import json
from enum import Enum


source = json.load(open("source/source.json", encoding='utf-8'))
btn_json = source["btn"]
msg_json = source["msg"]
API_TOKEN = '1647854818:AAHkxDcGaklU_DtBbkKRcwV-QGyuUtGVgnI'
#API_TOKEN = '1698570040:AAGvmUeVtpTKw18dn-VlTUAXDT04vWp-uhI'


class UserState(Enum):
    BACHELOR_WAITING_STATE = "BACHELOR_WAITING_STATE"
    MASTER_WAITING_STATE = "MASTER_WAITING_STATE"
    NULL_STATE ="NULL_STATE"