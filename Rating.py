from documents import button_check_handler
from source import coef, faculty_json, UserState, msg_json, btn_json
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

button_back_bachelor = btn_json["btn_back"]


def get_speciality(faculty):
    specialities = coef[faculty]
    specialities_string = []
    for speciality in specialities:
        specialities_string.append(speciality)
    return specialities_string


def get_subject(faculty, speciality):
    subjects = coef[faculty][speciality]
    subjects_arr = []
    for key in subjects:
        for subject in subjects[key]:
            if subject != "Коефіцієнт" and subject != "атестат" and subject != "Підготовчі курси":
                subjects_arr.append(subject)
    return subjects_arr


def calculate_final_rate(faculty, speciality, rate1, rate2, rate3, rate4, rate5):
    try:
        rate1 = float(rate1.replace(',', '.'))
        rate2 = float(rate2.replace(',', '.'))
        rate3 = float(rate3.replace(',', '.'))
        rate4 = float(rate4.replace(',', '.'))
        rate5 = float(rate5.replace(',', '.'))

        if rate1 < 100.0 or rate1 > 200.0 or rate2 < 100.0 or rate2 > 200.0 or \
                rate3 < 100.0 or rate3 > 200.0 or rate4 < 0.0 or rate4 > 12.0 or (rate5 < 100 and rate5 != 0) or rate5 > 200:
            raise Exception('Неправильні дані')

    except:
        return "Неправильні дані"
    rates = [rate1, rate2, rate3, rate5, rate4]
    result = 0
    subjects = coef[faculty][speciality]

    i = 0
    for position in subjects:
        result += float(list(subjects[position].values())[0]) * float(rates[i])
        i += 1

    kef = 0.1
    if "Атестат" in coef[faculty][speciality]:
        kef = 0.05
    result += kef * (100 + (float(rates[4]) - 2) * 10)

    return round(result, 3)


# RATING CALCULATION FUNCTION !!!
def button_rating_handler(update: Update, context: CallbackContext):
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
        text=msg_json["msg_choose_faculty"],
        reply_markup=reply_markup,
    )
    context.chat_data.update(state=UserState.SET_FACULTY)


def set_faculty(update: Update, context: CallbackContext):
    faculty = update.message.text
    specialities = get_speciality(faculty)
    context.chat_data.update(faculty=faculty, state=UserState.SET_SPECIALITY)
    inline_keyboard = []
    for speciality in specialities:
        inline_keyboard.append([InlineKeyboardButton(text=speciality, callback_data=specialities.index(speciality))])
    update.message.reply_text(text="Далі",
                              reply_markup=ReplyKeyboardMarkup(
                                  keyboard=[
                                      [
                                          KeyboardButton(text=button_back_bachelor)
                                      ],
                                  ],
                                  resize_keyboard=True
                              )
                              )
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
    context.chat_data.update(rate4=update.message.text)
    if "Підготовчі курси" in coef[context.chat_data.get("faculty")][context.chat_data.get("speciality")]:
        update.effective_message.reply_text(text="Введіть бал за підготовчі курси (у форматі ЗНО) ")
        context.chat_data.update(state=UserState.SET_RATE5)
    else:
        context.chat_data.update(rate5=0, state=UserState.NULL_STATE)
        update.effective_message.reply_text(text=calculate_final_rate(
            context.chat_data.get("faculty"),
            context.chat_data.get("speciality"),
            context.chat_data.get("rate1"),
            context.chat_data.get("rate2"),
            context.chat_data.get("rate3"),
            context.chat_data.get("rate4"),
            "0"
        ))


def set_rate5(update: Update, context: CallbackContext):
    update.effective_message.reply_text(text=calculate_final_rate(
        context.chat_data.get("faculty"),
        context.chat_data.get("speciality"),
        context.chat_data.get("rate1"),
        context.chat_data.get("rate2"),
        context.chat_data.get("rate3"),
        context.chat_data.get("rate4"),
        update.message.text
    ))
    context.chat_data.update(state=UserState.NULL_STATE)


def set_speciality(update: Update, context: CallbackContext):
    speciality_number = update.callback_query.data
    faculty = context.chat_data.get("faculty")
    speciality = get_speciality(faculty)[int(speciality_number)]

    subject = get_subject(context.chat_data.get("faculty"), speciality)[0]
    context.chat_data.update(state=UserState.SET_RATE1, speciality=speciality)
    update.effective_message.reply_text(text=(msg_json["msg_subject"].format(subject)))

speciality_array = ["ФГН(Факультет гуманітарних наук)", "ФПвН(Факультет правничих наук)", "Маркетинг/менеджмент", "Економіка/фінанси", "ФІ(Факультет інформатики)",
                    "ФПРН(Факультет природничих наук)", "Соціальна робота", "Міжнародні відносини", "Соціологія",
                    "Психологія", "Журналістика(зв'язки з громадськістю)", "Політологія"]

def callback_query_questions_handler(update: Update, context: CallbackContext):
    user = update.effective_user
    callback_data = update.callback_query.data
    chat_id = update.effective_message.chat_id
    message_id = update.effective_message.message_id
    update.effective_message.bot.deleteMessage(chat_id=chat_id, message_id=message_id)

    if context.chat_data.get("state") == UserState.SET_SPECIALITY_QUEUE_CONTRACT:
        context.chat_data.update(speciality_queue=speciality_array[int(callback_data)])
        return button_check_handler(update=update, context=context, state=UserState.SET_SPECIALITY_QUEUE_CONTRACT)
    if context.chat_data.get("state") == UserState.SET_SPECIALITY:
        set_speciality(update=update, context=context)
        return

    for key in btn_json:
        if callback_data == btn_json[key]:
            update.effective_message.reply_text(
                text=msg_json[key.replace("btn", "msg")]
            )
            break
