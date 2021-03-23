import telegram
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup, CallbackQuery, Bot
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from source import API_TOKEN, btn_json, msg_json
from queue.quickstart import add_to_table, check_in_queue


def log_error(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'Error:  {e}')
            raise e

    return inner


button_rating = btn_json["btn_rating"]

## RATING CALCULATION FUNCTION !!!

button_contact_bachelor = btn_json["btn_contacts"]


def button_contact_handler_bachelor(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_contact"]
    )


button_contact_master = btn_json["btn_contacts"]


def button_contact_handler_master(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_contact"]
    )


button_questions_bachelor = btn_json["btn_popular"]
button_questions_master = btn_json["btn_popular_master"]


def button_questions_handler_bachelor(update: Update, context: CallbackContext):
    inline_keyboard = [
        [
            InlineKeyboardButton(text=btn_json["btn_study_process"], callback_data=btn_json["btn_study_process"]),
            InlineKeyboardButton(text=btn_json["btn_vstup"], callback_data=btn_json["btn_vstup"])
        ],
        [
            InlineKeyboardButton(text=btn_json["btn_specialty"], callback_data=btn_json["btn_specialty"]),
            InlineKeyboardButton(text=btn_json["btn_hostels"], callback_data=btn_json["btn_hostels"])
        ],
        [
            InlineKeyboardButton(text=btn_json["btn_culture"], callback_data=btn_json["btn_culture"]),
            InlineKeyboardButton(text=btn_json["btn_infrastructure"], callback_data=btn_json["btn_infrastructure"])
        ],
        [
            InlineKeyboardButton(text=btn_json["btn_dates"], callback_data=btn_json["btn_dates"])
        ],
        [
            InlineKeyboardButton(text=btn_json["btn_documents"], callback_data=btn_json["btn_documents"])
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard)


def button_questions_handler_master(update: Update, context: CallbackContext):
    inline_keyboard = [
        [
            InlineKeyboardButton(text=btn_json["btn_study_process_master"],
                                 callback_data=btn_json["btn_study_process_master"]),
            InlineKeyboardButton(text=btn_json["btn_vstup_master"], callback_data=btn_json["btn_vstup_master"])
        ],
        [
            InlineKeyboardButton(text=btn_json["btn_specialty_master"], callback_data=btn_json["btn_specialty_master"]),
            InlineKeyboardButton(text=btn_json["btn_hostels_master"], callback_data=btn_json["btn_hostels_master"])
        ],
        [
            InlineKeyboardButton(text=btn_json["btn_culture_master"], callback_data=btn_json["btn_culture_master"]),
            InlineKeyboardButton(text=btn_json["btn_infrastructure_master"],
                                 callback_data=btn_json["btn_infrastructure_master"])
        ],
        [
            InlineKeyboardButton(text=btn_json["btn_dates_master"], callback_data=btn_json["btn_dates_master"])
        ],
        [
            InlineKeyboardButton(text=btn_json["btn_documents_master"], callback_data=btn_json["btn_documents_master"])
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard)


def callback_query_questions_handler(update: Update, context: CallbackContext):
    user = update.effective_user
    callback_data = update.callback_query.data

    chat_id = update.effective_message.chat_id

    if callback_data == btn_json["btn_study_process"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_student_process"]
        )
    elif callback_data == btn_json["btn_vstup"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_vstup"]
        )
    elif callback_data == btn_json["btn_dates"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_dates"]
        )
    elif callback_data == btn_json["btn_specialty"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_specialty"]
        )
    elif callback_data == btn_json["btn_hostels"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_hostels"]
        )
    elif callback_data == btn_json["btn_culture"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_culture"]
        )
    elif callback_data == btn_json["btn_infrastructure"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_infrastructure"]
        )
    elif callback_data == btn_json["btn_documents"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_documents"]
        )
    ###############################################################################################
    if callback_data == btn_json["btn_study_process_master"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_student_process"]
        )
    elif callback_data == btn_json["btn_vstup_master"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_vstup"]
        )
    elif callback_data == btn_json["btn_dates_master"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_dates"]
        )
    elif callback_data == btn_json["btn_specialty_master"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_specialty"]
        )
    elif callback_data == btn_json["btn_hostels_master"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_hostels"]
        )
    elif callback_data == btn_json["btn_culture_master"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_culture"]
        )
    elif callback_data == btn_json["btn_infrastructure_master"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_infrastructure"]
        )
    elif callback_data == btn_json["btn_documents_master"]:
        message_id = update.effective_message.message_id
        update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        update.effective_message.reply_text(
            text=msg_json["msg_documents"]
        )


button_queue_bachelor = btn_json["btn_queue"]
button_queue_master = btn_json["btn_queue_master"]

### QUEUE FUNCTION !!!

'''
button_back_bachelor = btn_json["btn_back"]
button_back_master = btn_json["btn_back_master"]

def button_back_bachelor_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_contact_bachelor),
                KeyboardButton(text=button_questions_bachelor)
            ],
            [
                KeyboardButton(text=button_queue_bachelor),
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
                KeyboardButton(text=button_contact_master),
                KeyboardButton(text=button_questions_bachelor)
            ],
            [
                KeyboardButton(text=button_queue_master),
                KeyboardButton(text=button_student_choice),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_choose"],
        reply_markup=reply_markup,
    )
'''


@log_error
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_bachelor:
        return button_bachelor_handler(update=update, context=context)
    if text == button_master:
        return button_master_handler(update=update, context=context)
    elif text == button_contact_bachelor:
        return button_contact_handler_bachelor(update=update, context=context)
    elif text == button_questions_bachelor:
        update.message.reply_text(
            text=msg_json["msg_question"],
            reply_markup=button_questions_handler_bachelor(update=update, context=context)
        )
    elif text == button_questions_master:
        update.message.reply_text(
            text=msg_json["msg_question"],
            reply_markup=button_questions_handler_master(update=update, context=context)
        )
    elif text == button_student_choice:
        return start(update=update, context=context)
    elif text == button_contact_master:
        return button_contact_handler_master(update=update, context=context)
    elif text == button_queue_bachelor:
        return  # QUEUE FOR BACHELORS
    elif text == button_queue_master:
        return  # QUEUE FOR MASTERS
    elif text == button_rating:
        return  # RATING CALCULATION
    '''    
    elif text == button_back_bachelor:
        return button_back_bachelor_handler(update=update, context=context)
    elif text == button_back_master:
        return button_back_master_handler(update=update, context=context)
    '''


button_bachelor = btn_json["btn_bachelor"]
button_master = btn_json["btn_master"]

button_student_choice = btn_json["btn_student_choice"]


def button_bachelor_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_contact_bachelor),
                KeyboardButton(text=button_questions_bachelor)
            ],
            [
                KeyboardButton(text=button_rating),
                KeyboardButton(text=button_student_choice),
            ],
            [
                KeyboardButton(text=button_queue_bachelor)
            ]
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

    inline_buttons_handler = CallbackQueryHandler(callback=callback_query_questions_handler)
    updater.dispatcher.add_handler(inline_buttons_handler)

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
