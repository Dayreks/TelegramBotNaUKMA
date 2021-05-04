from source import msg_json, btn_json, UserState
from tables import check_in_queue, add_to_table
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

button_queue_add = btn_json["btn_queue_add"]
button_queue_check = btn_json["btn_queue_check"]
button_queue_link = btn_json["btn_queue_link"]
button_dates = btn_json["btn_dates"]
button_required = btn_json["btn_documents"]
button_back_bachelor = btn_json["btn_back"]


def button_documents_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_dates),
                KeyboardButton(text=button_required)
            ],
            [
                KeyboardButton(text=button_queue_add),
                KeyboardButton(text=button_queue_check),
            ],
            [
                KeyboardButton(text=button_queue_link),
                KeyboardButton(text=btn_json["btn_back_questions"])
            ]
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_welcome"],
        reply_markup=reply_markup,
    )


def button_dates_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_dates"]
    )


def button_required_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_documents"]
    )


# QUEUE FUNCTION !!!
def button_queue_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_queue_add),
                KeyboardButton(text=button_queue_check)
            ],
            [
                KeyboardButton(text=button_back_bachelor),
                KeyboardButton(text=button_queue_link)
            ]
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_queue"],
        reply_markup=reply_markup,
    )


def button_queue_link_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_queue_link"]
    )


def button_check_handler(update: Update, context: CallbackContext):
    number = check_in_queue(update.message.chat_id)
    if number == -1:
        update.message.reply_text(msg_json["msg_not_in_queue"])
    elif number == 0:
        update.message.reply_text(msg_json["msg_queue_end"])
    else:
        update.message.reply_text(msg_json["msg_queue_number"].format(number))


def button_add_handler(update: Update, context: CallbackContext):
    update.message.reply_text(text=msg_json["msg_queue_start"])
    context.chat_data.update(state=UserState.BACHELOR_NAME_STATE)


def button_add_name_handler(update: Update, context: CallbackContext):
    context.chat_data.update(name=update.message.text)
    context.chat_data.update(state=UserState.BACHELOR_DEPARTMENT_STATE)
    update.message.reply_text(text=msg_json["msg_queue_department"])


def button_add_department_handler(update: Update, context: CallbackContext):
    context.chat_data.update(department=update.message.text)
    context.chat_data.update(state=UserState.BACHELOR_PHONE_STATE)
    update.message.reply_text(text=msg_json["msg_queue_phone"])


def button_add_phone_handler(update: Update, context: CallbackContext):
    context.chat_data.update(state=UserState.NULL_STATE)
    name = context.chat_data.get("name")
    department = context.chat_data.get("department")
    phone = update.message.text
    flag = add_to_table(update.message.chat_id, name, department, phone)
    if flag:
        update.message.reply_text(text=msg_json["msg_added"])
    else:
        update.message.reply_text(text=msg_json["msg_already_added"])


def parse_handler(update: Update, context: CallbackContext):
    state = context.chat_data.get("state")
    context.chat_data.update(state=UserState.NULL_STATE)
    message = update.message.text
    message = message.split(",")
    if len(message) != 3:
        context.chat_data.update(state=state)
        update.message.reply_text(text=msg_json["msg_queue_format_exception"])
    else:
        flag = add_to_table(update.message.chat_id, message[0], message[1], message[2])
        if flag:
            update.message.reply_text(text=msg_json["msg_added"])
        else:
            update.message.reply_text(text=msg_json["msg_already_added"])