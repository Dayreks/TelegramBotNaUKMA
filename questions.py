from source import btn_json, msg_json, UserState
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ParseMode
from telegram.ext import CallbackContext

button_zno = btn_json["btn_zno"]
button_vstup = btn_json["btn_vstup"]
button_study_process = btn_json["btn_study_process"]
button_hostels = btn_json["btn_hostels"]
button_culture = btn_json["btn_culture"]
button_infrastructure = btn_json["btn_infrastructure"]
button_operator = btn_json["btn_operator"]
button_exams = btn_json["btn_exams"]
button_vstup_master = btn_json["btn_vstup_master"]


def button_questions_handler_bachelor(update: Update, context: CallbackContext):
    context.chat_data.update(state=UserState.BACHELOR_QUESTIONS)
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_zno),
                KeyboardButton(text=button_vstup)
            ],
            [
                KeyboardButton(text=button_study_process),
                KeyboardButton(text=button_hostels)
            ],
            [
                KeyboardButton(text=button_culture),
                KeyboardButton(text=button_infrastructure)
            ],
            [
                KeyboardButton(text=button_operator),
            ],
            [
                KeyboardButton(text=btn_json["btn_back_questions"])
            ]
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_question"],
        reply_markup=reply_markup,
    )


def button_questions_handler_master(update: Update, context: CallbackContext):
    context.chat_data.update(state=UserState.MASTER_QUESTIONS)
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_exams),
                KeyboardButton(text=button_vstup_master)
            ],
            [
                KeyboardButton(text=button_study_process),
                KeyboardButton(text=button_hostels)
            ],
            [
                KeyboardButton(text=button_culture),
                KeyboardButton(text=button_infrastructure)
            ],
            [
                KeyboardButton(text=button_operator),
            ],
            [
                KeyboardButton(text=btn_json["btn_back_questions_master"])
            ]
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_question"],
        reply_markup=reply_markup,
    )


button_rozklad = btn_json["btn_rozklad"]
button_registration = btn_json["btn_registration"]
button_prep = btn_json["btn_prep"]
button_dpa_zno = btn_json["btn_dpa_zno"]
button_specifics = btn_json["btn_specifics"]
button_results = btn_json["btn_results"]
button_additional = btn_json["btn_additional"]
button_points = btn_json["btn_points"]
button_cost = btn_json["btn_cost"]
button_vstup_dates = btn_json["btn_vstup_dates"]
button_vstup_documents = btn_json["btn_vstup_documents"]
button_tot = btn_json["btn_tot"]
button_b_again = btn_json["btn_b_again"]
button_transfer = btn_json["btn_transfer"]
button_disciplines = btn_json["btn_disciplines"]
button_inp = btn_json["btn_inp"]
button_format = btn_json["btn_format"]
button_lection_seminar = btn_json["btn_lection_seminar"]
button_zalik_exam = btn_json["btn_zalik_exam"]
button_scholarship = btn_json["btn_scholarship"]
button_work_possibilities = btn_json["btn_work_possibilities"]
button_certificate = btn_json["btn_certificate"]
button_grade_professor = btn_json["btn_grade_professor"]
button_online = btn_json["btn_online"]
button_mobility = btn_json["btn_mobility"]
button_army = btn_json["btn_army"]
button_hostels_amount = btn_json["btn_hostels_amount"]
button_conditions = btn_json["btn_conditions"]
button_items_to_go = btn_json["btn_items_to_go"]
button_settlement = btn_json["btn_settlement"]
button_cost_living = btn_json["btn_cost_living"]
button_documents_settlement = btn_json["btn_documents_settlement"]
button_waivers = btn_json["btn_waivers"]
button_language = btn_json["btn_language"]
button_student_body = btn_json["btn_student_body"]
button_stud_organisations = btn_json["btn_stud_organisations"]
button_corporate_agreement = btn_json["btn_corporate_agreement"]
button_buildings = btn_json["btn_buildings"]
button_kmc = btn_json["btn_kmc"]
button_eat_nearby = btn_json["btn_eat_nearby"]
button_coffee = btn_json["btn_coffee"]
button_study = btn_json["btn_study"]
button_exams_master = btn_json["btn_exams_master"]
button_registration_evi = btn_json["btn_registration_evi"]
button_instruction = btn_json["btn_instruction"]
button_stages = btn_json["btn_stages"]
button_cost_study_master = btn_json["btn_cost_study_master"]
button_evi = btn_json["btn_evi"]
button_efvv = btn_json["btn_efvv"]
button_vstup_documents_master = btn_json["btn_vstup_documents_master"]

button_back_questions_menu = btn_json["btn_back_questions_menu"]
button_back_questions_menu_master = btn_json["btn_back_questions_menu_master"]


def details_handler(update: Update, context: CallbackContext, text):
    state = context.chat_data.get("state")
    if state == UserState.BACHELOR_QUESTIONS:
        back = button_back_questions_menu
    elif state == UserState.MASTER_QUESTIONS:
        back = button_back_questions_menu_master

###########STAS_BEGIN
    if text == button_zno:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_rozklad),
                    KeyboardButton(text=button_registration)
                ],
                [
                    KeyboardButton(text=button_prep),
                    KeyboardButton(text=button_dpa_zno)
                ],
                [
                    KeyboardButton(text=button_specifics),
                    KeyboardButton(text=button_results)
                ],
                [
                    KeyboardButton(text=button_additional),
                    KeyboardButton(text=back)
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_vstup:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_points),
                    KeyboardButton(text=button_cost)
                ],
                [
                    KeyboardButton(text=button_vstup_dates),
                    KeyboardButton(text=button_vstup_documents)
                ],
                [
                    KeyboardButton(text=button_tot),
                    KeyboardButton(text=button_b_again)
                ],
                [
                    KeyboardButton(text=button_transfer),
                    KeyboardButton(text=back)
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_exams:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_exams_master),
                    KeyboardButton(text=button_registration_evi)
                ],
                [
                    KeyboardButton(text=button_evi),
                    KeyboardButton(text=button_efvv)
                ],
                [
                    KeyboardButton(text=back)
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_vstup_master:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_instruction),
                    KeyboardButton(text=button_stages)
                ],
                [
                    KeyboardButton(text=button_vstup_documents_master),
                    KeyboardButton(text=button_b_again)
                ],
                [
                    KeyboardButton(text=button_transfer),
                    KeyboardButton(text=button_cost_study_master)
                ],
                [
                    KeyboardButton(text=back)
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_study_process:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_disciplines),
                    KeyboardButton(text=button_inp)
                ],
                [
                    KeyboardButton(text=button_format),
                    KeyboardButton(text=button_lection_seminar)
                ],
                [
                    KeyboardButton(text=button_zalik_exam),
                    KeyboardButton(text=button_scholarship)
                ],
                [
                    KeyboardButton(text=button_work_possibilities),
                    KeyboardButton(text=button_certificate)
                ],
                [
                    KeyboardButton(text=button_grade_professor),
                    KeyboardButton(text=button_online)
                ],
                [
                    KeyboardButton(text=button_mobility),
                    KeyboardButton(text=button_army)
                ],
                [
                        KeyboardButton(text=back)
                ]
            ],
            resize_keyboard=True,
        )
#############STAS_END

    elif text == button_hostels:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_hostels_amount),
                    KeyboardButton(text=button_conditions)
                ],
                [
                    KeyboardButton(text=button_items_to_go),
                    KeyboardButton(text=button_settlement)
                ],
                [
                    KeyboardButton(text=button_cost_living),
                    KeyboardButton(text=button_documents_settlement)
                ],
                [
                    KeyboardButton(text=button_waivers),
                    KeyboardButton(text=back)
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_culture:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_language),
                    KeyboardButton(text=button_student_body)
                ],
                [
                    KeyboardButton(text=button_stud_organisations),
                    KeyboardButton(text=button_corporate_agreement),
                ],
                [
                    KeyboardButton(text=back)
                ]
            ],
            resize_keyboard=True,
        )
    elif text == button_infrastructure:
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_buildings),
                    KeyboardButton(text=button_kmc)
                ],
                [
                    KeyboardButton(text=button_eat_nearby),
                    KeyboardButton(text=button_coffee)
                ],
                [
                    KeyboardButton(text=button_study),
                    KeyboardButton(text=back)
                ],
            ],
            resize_keyboard=True,
        )
    update.message.reply_text(
        text=msg_json["msg_question"],
        reply_markup=reply_markup
    )


def button_operator_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_operator"],
    )


def all_button_information_handler(update: Update, context: CallbackContext, text):
    for key in btn_json.keys():
        if text == btn_json[key]:
            text = key
            break

    text = text.replace("btn", "msg")
    update.message.reply_text(
        text=msg_json[text],
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


