from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from handlers import (
    greet_user, get_planet, calculator_user, user_coordinates,
    guess_number, send_cat_picture, get_date_visa, talk_to_me,
    check_user_photo, cat_picture_raiting
)
from anketa import anketa_start, anketa_name, anketa_rating, anketa_comment, anketa_skip, anketa_dontknow
from calculator_handler import calculator_start, calculator_user, calculator_dontknow
from game import start_play, guess_number, game_dontknow
from planets import planets_start, get_planet, planet_dontknow
from visa import visa_start, get_date_visa, visa_dontknow
import logging
import settings


logging.basicConfig(filename='bot.log', filemode='w', format='%(levelname)-8s %(asctime)s %(message)s', level=logging.DEBUG)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher

    anketa = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Заполнить анкету)$'), anketa_start)
        ],
        states={
            "name": [MessageHandler(Filters.text, anketa_name)],
            "rating": [MessageHandler(Filters.regex('^(1|2|3|4|5)$'), anketa_rating)],
            "comment": [
                CommandHandler("skip", anketa_skip),
                MessageHandler(Filters.text, anketa_comment)
            ]
        },
        fallbacks=[
            MessageHandler(Filters.text | Filters.video | Filters.photo | Filters.document | Filters.location, anketa_dontknow)
        ]
    )

    calculator = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Калькулятор)$'), calculator_start)
        ],
        states={
            "expression": [MessageHandler(Filters.text, calculator_user)],
        },
        fallbacks=[
            MessageHandler(Filters.text | Filters.video | Filters.photo | Filters.document | Filters.location, calculator_dontknow)
        ]
    )

    game_guess = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Игра в числа)$'), start_play)
        ],
        states={
            "number": [MessageHandler(Filters.text, guess_number)],
        },
        fallbacks=[
            MessageHandler(Filters.text | Filters.video | Filters.photo | Filters.document | Filters.location, game_dontknow)
        ]
    )

    visa_sity = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Ожидание визы)$'), visa_start)
        ],
        states={
            "city": [MessageHandler(Filters.text, get_date_visa)],
        },
        fallbacks=[
            MessageHandler(Filters.text | Filters.video | Filters.photo | Filters.document | Filters.location, visa_dontknow)
        ]
    )

    planet_user = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Расположение планет)$'), planets_start)
        ],
        states={
            "planet": [MessageHandler(Filters.text, get_planet)],
        },
        fallbacks=[
            MessageHandler(Filters.text | Filters.video | Filters.photo | Filters.document | Filters.location, planet_dontknow)
        ]
    )

    dp.add_handler(anketa)
    dp.add_handler(calculator)
    dp.add_handler(game_guess)
    dp.add_handler(visa_sity)
    dp.add_handler(planet_user)
    dp.add_handler(CommandHandler('start', greet_user))
    # dp.add_handler(CommandHandler('planet', get_planet))
    # dp.add_handler(CommandHandler('calculator', calculator_user))
    # dp.add_handler(CommandHandler('guess', guess_number))
    # dp.add_handler(CommandHandler('cat', send_cat_picture))
    # dp.add_handler(CommandHandler('visa', get_date_visa))
    dp.add_handler(CallbackQueryHandler(cat_picture_raiting, pattern="^(rating|)"))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'), send_cat_picture))
    dp.add_handler(MessageHandler(Filters.photo, check_user_photo))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot started")

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
