from source import coef, faculty_json, msg_json, UserState, btn_json
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
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
            subjects_arr.append(subject)
    return subjects_arr


def calculate_final_rate(faculty, speciality, rate1, rate2, rate3, rate4):
    try:
        rate1 = float(rate1)
        rate2 = float(rate2)
        rate3 = float(rate3)
        rate4 = float(rate4)
    except:
        return "Не правильні данні"
    rates = [rate1, rate2, rate3, rate4]
    result = 0
    subjects = coef[faculty][speciality]

    i = 0
    for position in subjects:
        result += float(list(subjects[position].values())[0]) * float(rates[i])
        i += 1
    result += 0.1 * float(rates[3])

    return result


# RATING CALCULATION FUNCTION !!!
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
