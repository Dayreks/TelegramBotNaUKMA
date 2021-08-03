from source import msg_json, btn_json, UserState
from tables import check_in_queue
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ParseMode
from telegram.ext import CallbackContext

button_queue_add = btn_json["btn_queue_add"]
button_queue_check_budget = btn_json["btn_queue_check_budget"]
button_queue_check_contract = btn_json["btn_queue_check_contract"]
button_queue_link_budget = btn_json["btn_queue_link_budget"]
button_queue_link = btn_json["btn_queue_link"]
button_queue_link_contract = btn_json["btn_queue_link_contract"]
button_dates = btn_json["btn_dates"]
button_required = btn_json["btn_documents"]
button_back_bachelor = btn_json["btn_back"]
button_cabinet = btn_json["btn_cabinet"]
button_cabinet_master = btn_json["btn_cabinet_master"]
button_originals = btn_json["btn_originals"]
button_originals_master = btn_json["btn_originals_master"]


def button_documents_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_required)
            ],
            [
                KeyboardButton(text=button_cabinet),
                KeyboardButton(text=button_originals),
            ],
            [
                KeyboardButton(text=btn_json["btn_back_questions"])
            ]
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_choose"],
        reply_markup=reply_markup,
    )


def button_documents_master_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_cabinet_master),
            ],
            [
                KeyboardButton(text=button_required),
                KeyboardButton(text=button_originals_master)
            ],
            [
                KeyboardButton(text=btn_json["btn_back_questions_master"])
            ]
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_choose"],
        reply_markup=reply_markup,
    )


# def button_dates_handler(update: Update, context: CallbackContext):
#   update.message.reply_text(
#       text=msg_json["msg_dates"]
#    )

def button_cabinet_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_cabinet"],
        parse_mode=ParseMode.HTML
    )


def button_cabinet_master_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_cabinet_master"],
        parse_mode=ParseMode.HTML
    )


def button_originals_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_originals"],
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


def button_originals_master_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_originals_master"],
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


def button_required_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_documents"],
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


# QUEUE FUNCTION !!!
def button_queue_handler(update: Update, context: CallbackContext):
    available = True
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_queue_link_budget),
                KeyboardButton(text=button_queue_link_contract),
            ],
            [
                KeyboardButton(text=button_queue_check_budget),
                KeyboardButton(text=button_queue_check_contract),
            ],
            [
                KeyboardButton(text=button_queue_link),
            ],
            [
                KeyboardButton(text=btn_json["btn_back_questions"])
            ]
        ],
        resize_keyboard=True,
    )
    if available:
        update.message.reply_text(
            text=msg_json["msg_queue"],
            reply_markup=reply_markup,
        )
    else:
        update.message.reply_text(
            text=msg_json["msg_queue_start"],
            parse_mode=ParseMode.HTML,
        )


def button_queue_link_handler_budget(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_queue_link_budget"],
        parse_mode=ParseMode.HTML,
    )


def button_queue_link_handler_contract(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_queue_link_contract"],
        parse_mode=ParseMode.HTML,
    )


def button_queue_link_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_queue_links"],
        parse_mode=ParseMode.HTML,
    )


def button_check_handler(update: Update, context: CallbackContext, state):
    context.chat_data.update(state=UserState.NULL_STATE)
    number = check_in_queue(state, context=context)
    if number == -1:
        if state == UserState.SET_SPECIALITY_QUEUE_CONTRACT:
            update.effective_message.reply_text(msg_json["msg_not_in_queue"])
        else:
            update.message.reply_text(msg_json["msg_not_in_queue"])
    elif number == 0:
        if state == UserState.SET_SPECIALITY_QUEUE_CONTRACT:
            update.effective_message.reply_text(msg_json["msg_queue_end"])
        else:
            update.message.reply_text(msg_json["msg_queue_end"])
    else:
        if state == UserState.SET_SPECIALITY_QUEUE_CONTRACT:
            update.effective_message.reply_text(msg_json["msg_queue_number"].format(number))
        else:
            update.message.reply_text(msg_json["msg_queue_number"].format(number))


"""def button_add_handler(update: Update, context: CallbackContext):
    update.message.reply_text(text=msg_json["msg_queue_name"], parse_mode=ParseMode.HTML)
    available = True
    if available:
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
"""
