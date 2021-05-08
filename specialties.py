from source import btn_json, msg_json
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ParseMode
from telegram.ext import CallbackContext

button_FI = btn_json["btn_FI"]
button_FPVN = btn_json["btn_FPVN"]
button_FPRN = btn_json["btn_FPRN"]
button_FEN = btn_json["btn_FEN"]
button_FSNST = btn_json["btn_FSNST"]
button_FGN = btn_json["btn_FGN"]

button_FI_master = btn_json["btn_FI_master"]
button_FPVN_master = btn_json["btn_FPVN_master"]
button_FPRN_master = btn_json["btn_FPRN_master"]
button_FEN_master = btn_json["btn_FEN_master"]
button_FSNST_master = btn_json["btn_FSNST_master"]
button_FGN_master = btn_json["btn_FGN_master"]

button_back_bachelor = btn_json["btn_back"]
button_back_master = btn_json["btn_back_master"]


def button_specialties_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_FI),
                KeyboardButton(text=button_FPVN)
            ],
            [
                KeyboardButton(text=button_FPRN),
                KeyboardButton(text=button_FEN),
            ],
            [
                KeyboardButton(text=button_FSNST),
                KeyboardButton(text=button_FGN),
            ],
            [
                KeyboardButton(text=button_back_bachelor)
            ]
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_choose_faculty"],
        reply_markup=reply_markup,
    )


def button_specialties_master_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_FI_master),
                KeyboardButton(text=button_FPVN_master)
            ],
            [
                KeyboardButton(text=button_FPRN_master),
                KeyboardButton(text=button_FEN_master),
            ],
            [
                KeyboardButton(text=button_FSNST_master),
                KeyboardButton(text=button_FGN_master),
            ],
            [
                KeyboardButton(text=button_back_master)
            ]
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_choose_faculty"],
        reply_markup=reply_markup
    )


button_ipz = btn_json["btn_ipz"]
button_computer = btn_json["btn_computer"]
button_math = btn_json["btn_math"]
button_history = btn_json["btn_history"]
button_philosophy = btn_json["btn_philosophy"]
button_philology_german = btn_json["btn_philology_german"]
button_philology_ukrainian = btn_json["btn_philology_ukrainian"]
button_culturology = btn_json["btn_culturology"]
button_marketing = btn_json["btn_marketing"]
button_managment = btn_json["btn_managment"]
button_finance = btn_json["btn_finance"]
button_economy = btn_json["btn_economy"]
button_politology = btn_json["btn_politology"]
button_sociology = btn_json["btn_sociology"]
button_social_work = btn_json["btn_social_work"]
button_connections = btn_json["btn_connections"]
button_psychology = btn_json["btn_psychology"]
button_international = btn_json["btn_international"]
button_ecology = btn_json["btn_ecology"]
button_biology = btn_json["btn_biology"]
button_chemistry = btn_json["btn_chemistry"]
button_physics = btn_json["btn_physics"]
button_law = btn_json["btn_law"]
button_history_master = btn_json["btn_history_master"]
button_archeology = btn_json["btn_archeology"]
button_udaika = btn_json["btn_udaika"]
button_philosophy_master = btn_json["btn_philosophy_master"]
button_philology_german_master = btn_json["btn_philology_german_master"]
button_philology_ukrainian_master = btn_json["btn_philology_ukrainian_master"]
button_philology_ukrainian_history_master = btn_json["btn_philology_ukrainian_history_master"]
button_culturology_master = btn_json["btn_culturology_master"]
button_ipz_master = btn_json["btn_ipz_master"]
button_computer_master = btn_json["btn_computer_master"]
button_math_master = btn_json["btn_math_master"]
button_system_analysis = btn_json["btn_system_analysis"]
button_marketing_master = btn_json["btn_marketing_master"]
button_management_strategy = btn_json["btn_management_strategy"]
button_management_energy = btn_json["btn_management_energy"]
button_management_business = btn_json["btn_management_business"]
button_finance_master = btn_json["btn_finance_master"]
button_economy_master = btn_json["btn_economy_master"]
button_politology_master = btn_json["btn_politology_master"]
button_politology_anticorruption = btn_json["btn_politology_anticorruption"]
button_sociology_master = btn_json["btn_sociology_master"]
button_social_work_master = btn_json["btn_social_work_master"]
button_journalism = btn_json["btn_journalism"]
button_journalism_links = btn_json["btn_journalism_links"]
button_psychology_master = btn_json["btn_psychology_master"]
button_management_health = btn_json["btn_management_health"]
button_management_healthcare = btn_json["btn_management_healthcare"]
button_ecology_master = btn_json["btn_ecology_master"]
button_biology_molecular = btn_json["btn_biology_molecular"]
button_biology_laboratory = btn_json["btn_biology_laboratory"]
button_physics_master = btn_json["btn_physics_master"]
button_chemistry_master = btn_json["btn_chemistry_master"]
button_law_master = btn_json["btn_law_master"]
button_public_control = btn_json["btn_public_control"]
button_public_control_communication = btn_json["btn_public_control_communication"]









def faculty_handler(update: Update, context: CallbackContext, text):
    if text == button_FI:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_FI_master),
                ],
                [
                    KeyboardButton(text=button_FPRN_master),
                ],
                [
                    KeyboardButton(text=button_FSNST_master),
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_FEN:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_FI_master),
                ],
                [
                    KeyboardButton(text=button_FPRN_master),
                ],
                [
                    KeyboardButton(text=button_FSNST_master),
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_FSNST:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_FI_master),
                ],
                [
                    KeyboardButton(text=button_FPRN_master),
                ],
                [
                    KeyboardButton(text=button_FSNST_master),
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_FGN:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_FI_master),
                ],
                [
                    KeyboardButton(text=button_FPRN_master),
                ],
                [
                    KeyboardButton(text=button_FSNST_master),
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_FPVN:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_FI_master),
                ],
                [
                    KeyboardButton(text=button_FPRN_master),
                ],
                [
                    KeyboardButton(text=button_FSNST_master),
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_FPRN:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_FI_master),
                ],
                [
                    KeyboardButton(text=button_FPRN_master),
                ],
                [
                    KeyboardButton(text=button_FSNST_master),
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_FPVN_master:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_FI_master),
                ],
                [
                    KeyboardButton(text=button_FPRN_master),
                ],
                [
                    KeyboardButton(text=button_FSNST_master),
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_FI_master:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_FI_master),
                ],
                [
                    KeyboardButton(text=button_FPRN_master),
                ],
                [
                    KeyboardButton(text=button_FSNST_master),
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_FPRN_master:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_FI_master),
                ],
                [
                    KeyboardButton(text=button_FPRN_master),
                ],
                [
                    KeyboardButton(text=button_FSNST_master),
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_FEN_master:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_FI_master),
                ],
                [
                    KeyboardButton(text=button_FPRN_master),
                ],
                [
                    KeyboardButton(text=button_FSNST_master),
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_FSNST_master:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_FI_master),
                ],
                [
                    KeyboardButton(text=button_FPRN_master),
                ],
                [
                    KeyboardButton(text=button_FSNST_master),
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_FGN_master:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_FI_master),
                ],
                [
                    KeyboardButton(text=button_FPRN_master),
                ],
                [
                    KeyboardButton(text=button_FSNST_master),
                ]
            ],
            resize_keyboard=True,
        )
    update.message.reply_text(
        text=msg_json["msg_choose_specialty"],
        reply_markup=reply_markup
    )
