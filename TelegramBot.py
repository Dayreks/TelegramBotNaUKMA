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
        text=msg_json["msg_contact"],
        reply_markup=menu(update=update, context=context),
    )


button_questions = btn_json["btn_popular"]
button_questions1 = btn_json["btn_study_process"]
button_questions2 = btn_json["btn_vstup"]
button_questions3 = btn_json["btn_specialty"]
button_questions4 = btn_json["btn_hostels"]
button_questions5 = btn_json["btn_culture"]
button_questions6 = btn_json["btn_infrastructure"]


# Inline buttons problems ?
def button_questions_handler(update: Update, context: CallbackContext):
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=button_questions1),
                InlineKeyboardButton(text=button_questions2)
            ],
            [
                InlineKeyboardButton(text=button_questions3),
            ]
        ]
    )

    update.message.reply_text(
        text=msg_json["msg_question"],
        reply_markup=reply_markup
    )


button_back = 'Назад'


def button_back_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_contact),
                KeyboardButton(text=button_questions)
            ],
            [
                KeyboardButton(text=button_back),
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
    if text == button_contact:
        return button_contact_handler(update=update, context=context)
    elif text == button_questions:
        return button_questions_handler(update=update, context=context)
    elif text == button_back:
        return button_back_handler(update=update, context=context)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_contact),
                KeyboardButton(text=button_questions)
            ],
            [
                KeyboardButton(text=button_back),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_welcome"],
        reply_markup=reply_markup,
    )


def menu(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_contact),
                KeyboardButton(text=button_questions)
            ],
            [
                KeyboardButton(text=button_back),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_choose"],  # Goes first instead of second after message
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
