from calculator import calculator
from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from utils import main_keyboard


def calculator_start(update, context):
    update.message.reply_text(
        "Введите выражение, которое необходимо посчитать!",
        reply_markup=ReplyKeyboardRemove()
    )
    return "expression"


def calculator_user(update, context):
    if len(update.message.text) < 2:
        update.message.reply_text(
            'Введите выражение, которое необхоимо посчитать!'
            )
        return "expression"
    else:
        update.message.reply_text(
            calculator(update.message.text),
            reply_markup=main_keyboard()
            )
    return ConversationHandler.END


def calculator_dontknow(update, context):
    update.message.reply_text('Я Вас не понимаю!')
