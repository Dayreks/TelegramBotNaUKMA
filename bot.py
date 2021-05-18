from Rating import get_speciality, calculate_final_rate, set_faculty, calculate_rate, button_rating_handler, set_rate1, \
    set_rate2, set_rate3, set_rate4, callback_query_questions_handler
from documents import button_documents_handler, button_queue_add, button_queue_check, button_queue_link, button_dates, \
    button_add_name_handler, button_add_department_handler, button_add_phone_handler, button_queue_handler, \
    button_add_handler, button_check_handler, button_queue_link_handler, button_required, \
    button_required_handler, button_cabinet_handler, button_originals_handler, button_cabinet_master_handler, \
    button_documents_master_handler
from questions import button_questions_handler_bachelor, button_questions_handler_master, details_handler, \
    button_operator_handler, button_rozklad, button_registration, button_prep, button_dpa_zno, \
    button_specifics, button_results, button_additional, all_button_information_handler, button_points, button_cost, \
    button_vstup_dates, button_vstup_documents, button_tot, button_b_again, button_transfer, button_army, \
    button_mobility, button_online, button_grade_professor, button_certificate, button_work_possibilities, \
    button_scholarship, button_zalik_exam, button_lection_seminar, button_format, button_inp, button_disciplines, \
    button_efvv, button_evi, button_registration_evi, button_exams_master, button_cost_study_master, button_instruction, \
    button_stages, button_vstup_documents_master, button_waivers, button_documents_settlement, button_cost_living, \
    button_settlement, button_items_to_go, button_conditions, button_hostels_amount, button_language, \
    button_student_body, button_corporate_agreement, button_stud_organisations, button_study, button_coffee, \
    button_eat_nearby, button_kmc, button_buildings
from source import API_TOKEN, btn_json, msg_json, UserState, faculty_json
from specialties import button_specialties_handler, button_specialties_master_handler, faculty_handler, \
    all_button_speciality_handler, button_ipz, button_computer, button_math, button_history, button_philology_german, \
    button_philosophy, button_philology_ukrainian, button_culturology, button_marketing, button_managment, \
    button_finance, button_economy, \
    button_politology, button_sociology, button_social_work, button_connections, button_psychology, \
    button_international, \
    button_ecology, button_biology, button_chemistry, button_physics, button_law, button_history_master, \
    button_philosophy_master, button_philology_german_master, button_philology_ukrainian_master, \
    button_culturology_master, button_ipz_master, button_computer_master, button_math_master, button_system_analysis, \
    button_marketing_master, \
    button_management_strategy, button_finance_master, \
    button_economy_master, \
    button_politology_master, button_sociology_master, button_social_work_master, \
    button_journalism, \
    button_psychology_master, button_management_health, \
    button_ecology_master, \
    button_biology_molecular, button_physics_master, button_chemistry_master, \
    button_law_master, \
    button_public_control, button_back_speciality, button_back_speciality_master
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup, ParseMode
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

button_start = btn_json["btn_start"]
button_rating = btn_json["btn_rating"]
button_contact = btn_json["btn_contacts"]
button_questions_bachelor = btn_json["btn_popular"]
button_questions_master = btn_json["btn_popular_master"]
button_queue_bachelor = btn_json["btn_queue"]
button_back_bachelor = btn_json["btn_back"]
button_back_master = btn_json["btn_back_master"]
button_back_speciality = btn_json["btn_back_speciality"]
button_back_speciality_master = btn_json["btn_back_speciality_master"]
button_bachelor = btn_json["btn_bachelor"]
button_master = btn_json["btn_master"]
button_student_choice = btn_json["btn_student_choice"]
button_fun = btn_json["btn_fun"]
button_specialties = btn_json["btn_specialties"]
button_specialties_master = btn_json["btn_specialties_master"]
button_documents = btn_json["btn_docs"]
button_documents_master = btn_json["btn_docs_master"]
button_cabinet = btn_json["btn_cabinet"]
button_cabinet_master = btn_json["btn_cabinet_master"]
button_originals = btn_json["btn_originals"]

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

button_info = btn_json["btn_info"]
button_vstup_info = btn_json["btn_vstup_info"]

button_zno = btn_json["btn_zno"]
button_vstup = btn_json["btn_vstup"]
button_study_process = btn_json["btn_study_process"]
button_hostels = btn_json["btn_hostels"]
button_culture = btn_json["btn_culture"]
button_infrastructure = btn_json["btn_infrastructure"]
button_operator = btn_json["btn_operator"]
button_exams = btn_json["btn_exams"]
button_vstup_master = btn_json["btn_vstup_master"]

button_back_questions_menu = btn_json["btn_back_questions_menu"]
button_back_questions_menu_master = btn_json["btn_back_questions_menu_master"]


def log_error(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'Error:  {e}')
            raise e

    return inner


def button_contact_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_info),
                KeyboardButton(text=button_vstup_info)
            ],
            [
                KeyboardButton(text=button_start),
            ]
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_choose"],
        reply_markup=reply_markup
    )


def button_info_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_contact_info"],
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


def button_vstup_info_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_contact_vstup"],
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


@log_error
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    state = context.chat_data.get("state")

    if text == button_start:
        return start(update=update, context=context)
    if text == button_back_bachelor:
        return button_bachelor_handler(update=update, context=context)
    if text == button_back_master:
        return button_master_handler(update=update, context=context)
    if state == UserState.SET_FACULTY:
        return set_faculty(update=update, context=context)
    if state == UserState.SET_RATE1:
        return set_rate1(update=update, context=context)
    if state == UserState.SET_RATE2:
        return set_rate2(update=update, context=context)
    if state == UserState.SET_RATE3:
        return set_rate3(update=update, context=context)
    if state == UserState.SET_RATE4:
        return set_rate4(update=update, context=context)
    if state == UserState.BACHELOR_NAME_STATE:
        return button_add_name_handler(update=update, context=context)
    if state == UserState.BACHELOR_DEPARTMENT_STATE:
        return button_add_department_handler(update=update, context=context)
    if state == UserState.BACHELOR_PHONE_STATE:
        return button_add_phone_handler(update=update, context=context)
    if text == button_bachelor:
        return button_bachelor_handler(update=update, context=context)
    if text == button_master:
        return button_master_handler(update=update, context=context)

    ############################################################

    elif text == button_contact:
        return button_contact_handler(update=update, context=context)
    elif text == button_info:
        return button_info_handler(update=update, context=context)
    elif text == button_vstup_info:
        return button_vstup_info_handler(update=update, context=context)
    ############################################################

    elif text == button_questions_bachelor:
        return button_questions_handler_bachelor(update=update, context=context)
    elif text == button_questions_master:
        return button_questions_handler_master(update=update, context=context)
    elif text == btn_json["btn_back_questions"]:
        return button_bachelor_handler(update=update, context=context)
    elif text == btn_json["btn_back_questions_master"]:
        return button_master_handler(update=update, context=context)
    elif text in [button_zno, button_exams, button_culture, button_study_process,
                  button_hostels, button_infrastructure, button_vstup, button_vstup_master]:
        return details_handler(update=update, context=context, text=text)
    elif text == button_back_questions_menu:
        return button_questions_handler_bachelor(update=update, context=context)
    elif text == button_back_questions_menu_master:
        return button_questions_handler_master(update=update, context=context)
    elif text == button_operator:
        return button_operator_handler(update=update, context=context)
    elif text in [button_rozklad, button_registration, button_prep, button_dpa_zno, button_specifics, button_results,
                  button_additional, button_points, button_cost, button_vstup_dates, button_vstup_documents, button_tot,
                  button_b_again, button_transfer, button_army, button_mobility, button_online, button_grade_professor,
                  button_certificate, button_work_possibilities, button_scholarship, button_zalik_exam,
                  button_lection_seminar, button_format, button_inp, button_disciplines, button_efvv, button_evi,
                  button_registration_evi, button_exams_master,
                  button_cost_study_master, button_instruction, button_stages, button_vstup_documents_master,
                  button_waivers, button_documents_settlement, button_cost_living, button_settlement,
                  button_items_to_go, button_conditions, button_hostels_amount,
                  button_corporate_agreement, button_student_body, button_language, button_stud_organisations,
                  button_study, button_coffee, button_eat_nearby, button_kmc, button_buildings]:
        return all_button_information_handler(update=update, context=context, text=text)

    ############################################################

    elif text == button_student_choice:
        return start(update=update, context=context)
    ############################################################

    elif text == button_queue_bachelor:
        return button_queue_handler(update=update, context=context)
    elif text == button_queue_add:
        context.chat_data.update(state=UserState.BACHELOR_WAITING_STATE)
        return button_add_handler(update=update, context=context)
    elif text == button_queue_check:
        return button_check_handler(update=update, context=context)
    elif text == button_queue_link:
        return button_queue_link_handler(update=update, context=context)

    ############################################################

    elif text == button_rating:
        return button_rating_handler(update=update, context=context)

    ############################################################

    elif text == button_documents:
        return button_documents_handler(update=update, context=context)
    elif text == button_documents_master:
        return button_documents_master_handler(update=update, context=context)
    elif text == button_cabinet:
        return button_cabinet_handler(update=update, context=context)
    elif text == button_cabinet_master:
        return button_cabinet_master_handler(update=update, context=context)
    elif text == button_required:
        return button_required_handler(update=update, context=context)
    elif text == button_originals:
        return button_originals_handler(update=update, context=context)

    ############################################################

    elif text == button_specialties:
        return button_specialties_handler(update=update, context=context)
    elif text == button_specialties_master:
        return button_specialties_master_handler(update=update, context=context)
    elif text in [button_FI, button_FPRN, button_FPVN, button_FSNST,
                  button_FEN, button_FGN, button_FEN_master, button_FSNST_master,
                  button_FGN_master, button_FI_master, button_FPRN_master, button_FPVN_master]:
        return faculty_handler(update=update, context=context, text=text)
    elif text in [button_ipz, button_computer, button_math, button_history, button_philosophy, button_philology_german,
                  button_philology_ukrainian, button_culturology, button_marketing, button_managment, button_finance,
                  button_economy,
                  button_politology, button_sociology, button_social_work, button_connections, button_psychology,
                  button_international,
                  button_ecology, button_biology, button_chemistry, button_physics, button_law, button_history_master,
                  button_philosophy_master, button_philology_german_master,
                  button_philology_ukrainian_master,
                  button_culturology_master, button_ipz_master, button_computer_master, button_math_master,
                  button_system_analysis, button_marketing_master,
                  button_management_strategy,
                  button_finance_master, button_economy_master,
                  button_politology_master, button_sociology_master,
                  button_social_work_master, button_journalism,
                  button_psychology_master, button_management_health,
                  button_ecology_master,
                  button_biology_molecular, button_physics_master, button_chemistry_master,
                  button_law_master,
                  button_public_control]:
        return all_button_speciality_handler(update=update, context=context, text=text)
    elif text == button_back_speciality:
        return button_specialties_handler(update=update, context=context)
    elif text == button_back_speciality_master:
        return button_specialties_master_handler(update=update, context=context)


def button_bachelor_handler(update: Update, context: CallbackContext):
    context.chat_data.update(state=UserState.NULL_STATE)
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_rating)
            ],
            [
                KeyboardButton(text=button_specialties),
                KeyboardButton(text=button_questions_bachelor)

            ],
            [
                KeyboardButton(text=button_documents)
            ],
            [
                KeyboardButton(text=button_student_choice)
            ]
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_welcome"],
        reply_markup=reply_markup,
    )
    context.chat_data.update(state=UserState.NULL_STATE)


def button_master_handler(update: Update, context: CallbackContext):
    context.chat_data.update(state=UserState.NULL_STATE)
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_specialties_master),
                KeyboardButton(text=button_documents_master)
            ],
            [
                KeyboardButton(text=button_questions_master)
            ],
            [
                KeyboardButton(text=button_student_choice),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_welcome"],
        reply_markup=reply_markup,
    )


def start(update: Update, context: CallbackContext):
    context.chat_data.update(state=UserState.NULL_STATE)
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_bachelor),
                KeyboardButton(text=button_master)
            ],
            [
                KeyboardButton(text=button_contact)
            ],
            [
                KeyboardButton(text=button_fun)
            ]

        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_choose"],
        reply_markup=reply_markup,
    )


def main():
    print('Start')
    updater = Updater(
        token=API_TOKEN,
        use_context=True,
    )

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    print(updater.bot.get_me())

    inline_buttons_handler = CallbackQueryHandler(callback=callback_query_questions_handler)
    updater.dispatcher.add_handler(inline_buttons_handler)

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
