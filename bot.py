from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import (
    greet_user, get_planet, calculator_user, user_coordinates,
    guess_number, send_cat_picture, get_date_visa, talk_to_me
)
from conversation import conv_hendler
from utils import (get_smile, main_keyboard)
import logging
import settings


logging.basicConfig(filename='bot.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', get_planet))
    dp.add_handler(CommandHandler('calculator', calculator_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(CommandHandler('visa', get_date_visa))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'), send_cat_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Калькулятор)$'), conv_hendler))
    dp.add_handler(MessageHandler(Filters.regex('^(Игра в числа)$'), conv_hendler))
    dp.add_handler(MessageHandler(Filters.regex('^(Ожидание визы)$'), conv_hendler))
    dp.add_handler(MessageHandler(Filters.regex('^(Расположение планет)$'), conv_hendler))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot started")

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()



# https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid=P115&aid=VisaWaitTimesHomePage