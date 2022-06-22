from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from utils import main_keyboard
from wait_visa import city


def visa_start(update, context):
    update.message.reply_text(
        "Введите город на английском языке",
        reply_markup=ReplyKeyboardRemove()
    )
    return "city"


def get_date_visa(update, context):
    print(update.message.text)
    user_city = str(update.message.text).title()
    update.message.reply_text(city(user_city), reply_markup=main_keyboard())
    return ConversationHandler.END


def visa_dontknow(update, context):
    update.message.reply_text('Я Вас не понимаю!')
