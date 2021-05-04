import json

from Rating import get_speciality, get_subject
from source import btn_json, UserState, msg_json
from telegram import InlineKeyboardButton, Update, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CallbackContext


def button_questions_handler_bachelor(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=btn_json["btn_zno"]),
                KeyboardButton(text=btn_json["btn_vstup"])
            ],
            [
                KeyboardButton(text=btn_json["btn_study_process"]),
                KeyboardButton(text=btn_json["btn_hostels"])
            ],
            [
                KeyboardButton(text=btn_json["btn_culture"]),
                KeyboardButton(text=btn_json["btn_infrastructure"])
            ],
            [
                KeyboardButton(text=btn_json["btn_operator"]),
                KeyboardButton(text=btn_json["btn_back_questions"])
            ],
        ]
    )
    update.message.reply_text(
        text=msg_json["msg_question"],
        reply_markup=reply_markup,
    )


def button_questions_handler_master(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=btn_json["btn_exams"]),
                KeyboardButton(text=btn_json["btn_vstup_master"])
            ],
            [
                KeyboardButton(text=btn_json["btn_study_process_master"]),
                KeyboardButton(text=btn_json["btn_hostels"])
            ],
            [
                KeyboardButton(text=btn_json["btn_culture"]),
                KeyboardButton(text=btn_json["btn_infrastructure"])
            ],
            [
                KeyboardButton(text=btn_json["btn_operator"]),
                KeyboardButton(text=btn_json["btn_back_questions_master"])
            ],
        ]
    )
    update.message.reply_text(
        text=msg_json["msg_question"],
        reply_markup=reply_markup,
    )


"""
def set_speciality(update: Update, context: CallbackContext):
    speciality_number = update.callback_query.data
    faculty = context.chat_data.get("faculty")
    speciality = get_speciality(faculty)[int(speciality_number)]
    subjects = get_subject(faculty, speciality)
    context.chat_data.update(speciality=speciality, state=UserState.SET_RATE)

    main_str = subjects[0] + ", " + subjects[1]
    optional_str = ""
    i = 2
    while i < len(subjects) - 1:
        optional_str = optional_str + subjects[i] + ", "
        i += 1
    optional_str += subjects[len(subjects) - 1]
    out_msg = msg_json["msg_subject"] % (main_str, optional_str)
    print(out_msg)
    update.effective_message.reply_text(
        text=out_msg
    )




def callback_query_questions_handler(update: Update, context: CallbackContext):
    user = update.effective_user
    callback_data = update.callback_query.data
    chat_id = update.effective_message.chat_id

    message_id = update.effective_message.message_id
    update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)

    if context.chat_data.get("state") == UserState.SET_SPECIALITY:
        set_speciality(update=update, context=context)
        return

    for key in btn_json:
        if callback_data == btn_json[key]:
            update.effective_message.reply_text(
                text=msg_json[key.replace("btn", "msg")]
            )
            break
"""
