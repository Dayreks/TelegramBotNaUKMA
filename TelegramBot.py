from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


def log_error(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'Error:  {e}')
            raise e

    return inner


button_contact = 'Наші контакти'


def button_contact_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='До кого я можу звернутися з питаннями щодо вступної кампанії? '
             '\n-Вступ НаУКМА (додати посилання: інста, тікток ..)'
             '\n-гаряча лінія (?)'
             '\n-контакти певних відділів (додати посилання)'
             '\n'
             '\nДе ще можна знайти відповіді на запитання? Більше відповідей на запитання шукай:'
             '\nhttps://vstup.ukma.edu.ua/abituriyentam-pro-naukma/zapytannya-ta-vidpovidi/'
             '\nhttps://www.ukma.edu.ua/index.php/kontakti/153-admission/808-pitannya',
        reply_markup=menu(update=update, context=context),
    )


button_questions = 'Найбільш популярні запитання'
button_questions1 = 'Навчальний процес'
button_questions2 = 'Вступна кампанія'
button_questions3 = 'Спеціальність'
button_questions4 = 'Гуртожиток'
button_questions5 = 'Корпоративна культура'
button_questions6 = 'Інфраструктура КМА'


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
        text='Запитання:',
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
        text='Оберіть вашу дію:',
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
        text='Вітаємо, майбутній студент Могилянки!'
             '\nЧим можу допомогти ?',
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
        text='Оберіть вашу дію:',  # Goes first instead of second after message
        reply_markup=reply_markup,
    )


def main():
    print('Start')
    updater = Updater(
        token='1672955809:AAHbwvoMU9mSGdNJDCPtK63M86qDxoXtmfI',
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
