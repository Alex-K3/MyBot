import logging
from wsgiref.handlers import format_date_time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from datetime import datetime 
from calculator import calculator

logging.basicConfig(filename='bot.log', format='%(asctime)s - %(message)s', level=logging.INFO)



def greet_user(update, contex):
    print('Вызван /start')
    update.message.reply_text('Здравствуй, пользователь!')
    print(update.message)


def get_planet(update: Update, contex: CallbackContext):
    list_word = update.message.text.split(' ')
    if len(list_word) == 1:
        update.message.reply_text('Напишите название планеты на Англ. языкe')
    elif len(list_word) == 2:
        planet = list_word[1]
        print(planet)
        class_planet = getattr(ephem, planet)()
        current_time = datetime.now().strftime("%Y/%m/%d") 
        class_planet.compute(current_time)
        print(class_planet)
        update.message.reply_text(ephem.constellation(class_planet))



def calculator_user(update: Update, contex):
    cal_user = update.message.text.split(' ')
    print(cal_user)
    if len(cal_user[1]) == 1:
        update.message.reply_text('Введите выражение, которое необхоимо посчитать')
    else:
        update.message.reply_text(calculator(cal_user[1]))


                
def talk_to_me(update, contex):
    text = update.message.text
    print(text)
    update.message.reply_text(text)



def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', get_planet))
    dp.add_handler(CommandHandler('calculator', calculator_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot started")

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
