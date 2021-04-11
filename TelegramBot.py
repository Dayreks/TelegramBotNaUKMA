import telegram
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup, CallbackQuery, Bot
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from source import API_TOKEN, btn_json, msg_json, UserState, faculty_json
from tables import add_to_table, check_in_queue, UserType
from Rating import get_speciality, get_subject, calculate_final_rate

button_rating = btn_json["btn_rating"]
button_contact_bachelor = btn_json["btn_contacts"]
button_contact_master = btn_json["btn_contacts"]
button_questions_bachelor = btn_json["btn_popular"]
button_questions_master = btn_json["btn_popular_master"]
button_queue_bachelor = btn_json["btn_queue"]
button_queue_add = btn_json["btn_queue_add"]
button_queue_check = btn_json["btn_queue_check"]
button_queue_link = btn_json["btn_queue_link"]
button_back_bachelor = btn_json["btn_back"]
button_bachelor = btn_json["btn_bachelor"]
button_master = btn_json["btn_master"]
button_student_choice = btn_json["btn_student_choice"]


def log_error(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'Error:  {e}')
            raise e

    return inner


## RATING CALCULATION FUNCTION !!!
def button_rating_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_choose_faculty"]
    )

    keyboard = []
    temp = []
    counter = 0
    for key in faculty_json:
        temp.append(KeyboardButton(text=faculty_json[key]))
        counter += 1
        if counter == 2:
            keyboard.append(temp)
            temp = []
            counter = 0
    keyboard.append([KeyboardButton(text=button_back_bachelor)])
    reply_markup = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=msg_json["msg_welcome"],
        reply_markup=reply_markup,
    )
    context.chat_data.update(state=UserState.SET_FACULTY)


def button_contact_handler_bachelor(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_contact"]
    )


def button_contact_handler_master(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=msg_json["msg_contact"]
    )


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


def set_speciality(update: Update, context: CallbackContext):
    speciality_number = update.callback_query.data
    faculty = context.chat_data.get("faculty")
    speciality = get_speciality(faculty)[int(speciality_number)]

    subject = get_subject(context.chat_data.get("faculty"), speciality)[0]
    context.chat_data.update(state=UserState.SET_RATE1, speciality=speciality)
    update.effective_message.reply_text(text=(msg_json["msg_subject"].format(subject)))


def callback_query_questions_handler(update: Update, context: CallbackContext):
    user = update.effective_user
    callback_data = update.callback_query.data
    chat_id = update.effective_message.chat_id

    message_id = update.effective_message.message_id
    update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)

    if context.chat_data.get("state") == UserState.SET_SPECIALITY:
        set_speciality(update=update, context=context)
        return

    for key in btn_json:
        if callback_data == btn_json[key]:
            update.effective_message.reply_text(
                text=msg_json[key.replace("btn", "msg")]
            )
            break


### QUEUE FUNCTION !!!
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


def set_faculty(update: Update, context: CallbackContext):
    faculty = update.message.text
    specialities = get_speciality(faculty)
    context.chat_data.update(faculty=faculty, state=UserState.SET_SPECIALITY)
    inline_keyboard = []
    for speciality in specialities:
        inline_keyboard.append([InlineKeyboardButton(text=speciality, callback_data=specialities.index(speciality))])
    update.message.reply_text(text="Далі",
                              reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=button_back_bachelor)]]))
    update.message.reply_text(text=msg_json["msg_choose_speciality"],
                              reply_markup=InlineKeyboardMarkup(inline_keyboard))


def calculate_rate(update: Update, context: CallbackContext):
    text = update.message.text
    result = calculate_final_rate(context.chat_data.get("faculty"), context.chat_data.get("speciality"), text)
    context.chat_data.update(state=UserState.NULL_STATE)
    update.message.reply_text(text=result)


def set_rate1(update: Update, context: CallbackContext):
    rate = update.message.text
    context.chat_data.update(rate1=rate, state=UserState.SET_RATE2)
    subject = get_subject(context.chat_data.get("faculty"), context.chat_data.get("speciality"))[1]
    update.effective_message.reply_text(text=(msg_json["msg_subject"].format(subject)))


def set_rate2(update: Update, context: CallbackContext):
    rate = update.message.text
    context.chat_data.update(rate2=rate, state=UserState.SET_RATE3)
    subjects = get_subject(context.chat_data.get("faculty"), context.chat_data.get("speciality"))
    subject = ""
    i = 2
    while i < len(subjects) - 1:
        subject += subjects[i] + ", "
        i += 1
    subject += subjects[len(subjects) - 1]
    update.effective_message.reply_text(text=(msg_json["msg_subject_multiple"].format(subject)))


def set_rate3(update: Update, context: CallbackContext):
    rate = update.message.text
    context.chat_data.update(rate3=rate, state=UserState.SET_RATE4)
    update.effective_message.reply_text(text=msg_json["msg_school_rate"])


def set_rate4(update: Update, context: CallbackContext):
    update.effective_message.reply_text(text=calculate_final_rate(
        context.chat_data.get("faculty"),
        context.chat_data.get("speciality"),
        context.chat_data.get("rate1"),
        context.chat_data.get("rate2"),
        context.chat_data.get("rate3"),
        update.message.text
    ))
    context.chat_data.update(state=UserState.NULL_STATE)


@log_error
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    state = context.chat_data.get("state")
    if text == button_back_bachelor:
        return button_bachelor_handler(update=update, context=context)
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
    elif text == button_contact_bachelor:
        return button_contact_handler_bachelor(update=update, context=context)
    ############################################################
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
