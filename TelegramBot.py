from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from source import API_TOKEN, btn_json, msg_json


def log_error(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'Error:  {e}')
            raise e

    return inner


button_contact = btn_json["btn_contacts"]


def button_contact_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_contact"]
    )
    button_back_bachelor_handler(update=update, context=context)


button_questions = btn_json["btn_popular"]
button_questions1 = btn_json["btn_study_process"]
button_questions2 = btn_json["btn_vstup"]
button_questions3 = btn_json["btn_specialty"]
button_questions4 = btn_json["btn_hostels"]
button_questions5 = btn_json["btn_culture"]
button_questions6 = btn_json["btn_infrastructure"]


def button_questions_handler(update: Update, context: CallbackContext):
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=button_questions1, callback_data='111'),
                InlineKeyboardButton(text=button_questions2, callback_data='222')
            ],
            [
                InlineKeyboardButton(text=button_questions3, callback_data='333'),
                InlineKeyboardButton(text=button_questions4, callback_data='444')
            ],
            [
                InlineKeyboardButton(text=button_questions5, callback_data='555'),
                InlineKeyboardButton(text=button_questions6, callback_data='666')
            ]
        ]
    )

    update.message.reply_text(
        text=msg_json["msg_question"],
        reply_markup=reply_markup
    )


button_back_bachelor = btn_json["btn_back"]
button_back_master = btn_json["btn_back"]


def button_back_bachelor_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_contact),
                KeyboardButton(text=button_questions)
            ],
            [
                KeyboardButton(text=button_student_choice),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_choose"],
        reply_markup=reply_markup,
    )


def button_back_master_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_contact),
                KeyboardButton(text=button_questions)
            ],
            [
                KeyboardButton(text=button_student_choice),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_choose"],
        reply_markup=reply_markup,
    )


@log_error
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_bachelor:
        return button_bachelor_handler(update=update, context=context)
    elif text == button_master:
        return button_master_handler(update=update, context=context)
    elif text == button_contact:
        return button_contact_handler(update=update, context=context)
    elif text == button_questions:
        return button_questions_handler(update=update, context=context)
    elif text == button_back_bachelor:
        return button_back_bachelor_handler(update=update, context=context)
    elif text == button_back_master:
        return button_back_master_handler(update=update, context=context)
    elif text == button_student_choice:
        return start(update=update, context=context)


button_bachelor = btn_json["btn_bachelor"]
button_master = btn_json["btn_master"]


def menu(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_contact),
                KeyboardButton(text=button_questions)
            ],
            [
                KeyboardButton(text=button_student_choice),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_choose"],
        reply_markup=reply_markup,
    )


button_student_choice = btn_json["button_student_choice"]


def button_bachelor_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_contact),
                KeyboardButton(text=button_questions)
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


def button_master_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_contact),
                KeyboardButton(text=button_questions)
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
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_bachelor),
                KeyboardButton(text=button_master)
            ],

        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_level"],
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

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
