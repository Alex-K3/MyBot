from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters, Updater
from handlers import (
    get_planet, calculator_user,
    guess_number, get_date_visa
)


def conv_hendler(update, context):
    user_text = update.message.text
    if user_text == 'Kалькулятор':
        update.message.reply_text('Введите выражение, которое необходимо посчитать')
        user_text = update.message.text
        print(user_text)
        calculator_user(user_text)
    elif user_text == 'Игра в числа':
        update.message.reply_text('Введите Ваше число')
        user_text = update.message.text
        print(user_text)
        guess_number(user_text)
    elif user_text == 'Ожидание визы':
        update.message.reply_text('Введите город на английском языке, для которого необходимо узнать ожидание')
        user_text = update.message.text
        print(user_text)
        get_date_visa(user_text)
    elif user_text == 'Расположение планет':
        update.message.reply_text('Введите планету на английском языке, о которой Вы хотите узнать космическое положение')
        user_text = update.message.text
        print(user_text)
        get_planet(user_text)

    # ch = ConversationHandler(
    #     entry_points=[CommandHandler(comand)]
    #     states={
    #         1: [MessageHandler(Filters.regex('^(Калькулятор)$'), calculator_user(), pass_user_data=True)],
    #         2: [MessageHandler(Filters.regex('^(Игра в числа)$'), guess_number(), pass_user_data=True)],
    #         3: [MessageHandler(Filters.regex('^(Ожидание визы)$'), get_date_visa(), pass_user_data=True)],
    #         4: [MessageHandler(Filters.regex('^(Расположение планет)$'), get_planet(), pass_user_data=True)],
    #     }
    # )
