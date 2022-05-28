from email import message
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from datetime import datetime 
from calculator import calculator
from random import randint, choice
from glob import glob
from emoji import emojize

logging.basicConfig(filename='bot.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)



def greet_user(update, context):
    print('Вызван /start')
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f'Здравствуй, пользователь {context.user_data["emoji"]}!')
    print(update.message)


def get_planet(update: Update, contex: CallbackContext):
    list_word = update.message.text.split(' ')
    if len(list_word) == 1:
        update.message.reply_text('Напишите название планеты на Англ. языкe')
    elif len(list_word) == 2:
        planet = list_word[1].title()
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



def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Выше число {user_number}, мое {bot_number}, вы выиграли'
    elif user_number == bot_number:
        message = f'Выше число {user_number}, мое {bot_number}, ничья'
    else:
        message = f'Выше число {user_number}, мое {bot_number}, вы проиграли'
    return message



def guess_number(update, context):
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message = 'Введи число'
    print(context.args)
    update.message.reply_text(message)



def send_cat_picture(update, context):
    cat_photo_list = glob('images/*.jp*g')
    cat_photo_filename = choice(cat_photo_list)
    print(cat_photo_filename)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_photo_filename, 'rb'))


                
def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f'{text} {context.user_data["emoji"]}')



def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']



def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', get_planet))
    dp.add_handler(CommandHandler('calculator', calculator_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot started")

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
