from source import btn_json, msg_json
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
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
            ],
            [
                KeyboardButton(text=btn_json["btn_back_questions"])
            ]
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
                KeyboardButton(text=btn_json["btn_study_process"]),
                KeyboardButton(text=btn_json["btn_hostels"])
            ],
            [
                KeyboardButton(text=btn_json["btn_culture"]),
                KeyboardButton(text=btn_json["btn_infrastructure"])
            ],
            [
                KeyboardButton(text=btn_json["btn_operator"]),
            ],
            [
                KeyboardButton(text=btn_json["btn_back_questions_master"])
            ]
        ]
    )
    update.message.reply_text(
        text=msg_json["msg_question"],
        reply_markup=reply_markup,
    )

