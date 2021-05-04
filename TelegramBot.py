from Rating import get_speciality, calculate_final_rate, set_faculty, calculate_rate, button_rating_handler
from documents import button_documents_handler, button_queue_add, button_queue_check, button_queue_link, button_dates, \
    button_add_name_handler, button_add_department_handler, button_add_phone_handler, button_queue_handler, \
    button_add_handler, button_check_handler, button_queue_link_handler, button_dates_handler, button_required, \
    button_required_handler
from questions import button_questions_handler_bachelor, button_questions_handler_master
from source import API_TOKEN, btn_json, msg_json, UserState, faculty_json
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

button_rating = btn_json["btn_rating"]
button_contact_bachelor = btn_json["btn_contacts"]
button_contact_master = btn_json["btn_contacts"]
button_questions_bachelor = btn_json["btn_popular"]
button_questions_master = btn_json["btn_popular_master"]
button_queue_bachelor = btn_json["btn_queue"]
button_back_bachelor = btn_json["btn_back"]
button_bachelor = btn_json["btn_bachelor"]
button_master = btn_json["btn_master"]
button_student_choice = btn_json["btn_student_choice"]
button_fun = btn_json["btn_fun"]
button_specialties = btn_json["btn_specialties"]
button_documents = btn_json["btn_docs"]


def log_error(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'Error:  {e}')
            raise e

    return inner


def button_contact_handler_bachelor(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_contact"]
    )


def button_contact_handler_master(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_contact"]
    )


@log_error
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    state = context.chat_data.get("state")

    if text == button_back_bachelor:
        return button_bachelor_handler(update=update, context=context)
    if state == UserState.SET_FACULTY:
        return set_faculty(update=update, context=context)
    if state == UserState.SET_RATE:
        return calculate_rate(update=update, context=context)
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
    elif text == button_contact_bachelor:
        return button_contact_handler_bachelor(update=update, context=context)

    ############################################################

    elif text == button_questions_bachelor:
        return button_questions_handler_bachelor(update=update, context=context)
    elif text == button_questions_master:
        return button_questions_handler_master(update=update, context=context)
    elif text == btn_json["btn_back_questions"]:
        return button_bachelor_handler(update=update, context=context)
    elif text == btn_json["btn_back_questions_master"]:
        return button_master_handler(update=update, context=context)

    ############################################################

    elif text == button_student_choice:
        return start(update=update, context=context)
    elif text == button_contact_master:
        return button_contact_handler_master(update=update, context=context)

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
    elif text == button_dates:
        return button_dates_handler(update=update, context=context)
    elif text == button_required:
        return button_required_handler(update=update, context=context)


def button_bachelor_handler(update: Update, context: CallbackContext):
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
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_contact_master),
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
                KeyboardButton(text=button_contact_bachelor)
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

    # inline_buttons_handler = CallbackQueryHandler(callback=callback_query_questions_handler)
    # updater.dispatcher.add_handler(inline_buttons_handler)

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
