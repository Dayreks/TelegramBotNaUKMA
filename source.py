import json
from enum import Enum


source = json.load(open("source/source.json", encoding='utf-8'))
btn_json = source["btn"]
msg_json = source["msg"]
faculty_json = source["btn"]["fac_list"]

coef = json.load(open("source/coef.json", encoding='utf-8'))

API_TOKEN = '1647854818:AAHkxDcGaklU_DtBbkKRcwV-QGyuUtGVgnI'
# API_TOKEN = '1698570040:AAGvmUeVtpTKw18dn-VlTUAXDT04vWp-uhI'


class UserState(Enum):
    BACHELOR_WAITING_STATE = "BACHELOR_WAITING_STATE"
    BACHELOR_NAME_STATE = "BACHELOR_NAME_STATE"
    BACHELOR_DEPARTMENT_STATE = "BACHELOR_DEPARTMENT_STATE"
    BACHELOR_PHONE_STATE = "BACHELOR_PHONE_STATE"
    MASTER_WAITING_STATE = "MASTER_WAITING_STATE"
    BACHELOR_ADD_STATE = "BACHELOR_ADD_STATE"
    NULL_STATE ="NULL_STATE"
    EXAM_PTS_ENTRY_STATE = "EXAM_PTS_ENTRY_STATE"
    SET_FACULTY = "SET_FACULTY"
    SET_SPECIALITY = "SET_SPECIALITY"
    SET_RATE = "SET_RATE"
    SET_RATE1 = "SET_RATE1"
    SET_RATE2 = "SET_RATE2"
    SET_RATE3 = "SET_RATE3"
    SET_RATE4 = "SET_RATE4"
    