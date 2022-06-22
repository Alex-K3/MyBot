from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from utils import main_keyboard, play_random_numbers

def start_play(update, context):
    update.message.reply_text(
        "Введите Ваше число",
        reply_markup = ReplyKeyboardRemove()
    )
    return "number"

def guess_number(update, context):
    print(update.message.text)
    if update.message.text:
        try:
            user_number = int(update.message.text)
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            update.message.reply_text("Введите Ваше число")
            return "number"
    else:
        message = 'Введи число!'
        return "number"
    print(update.message.text)
    update.message.reply_text(message, reply_markup = main_keyboard())
    return ConversationHandler.END

def game_dontknow(update, context):
    update.message.reply_text('Я Вас не понимаю!')