from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from utils import main_keyboard
from datetime import datetime
import ephem

reply_keyboards = [
        ['Mercury', 'Venus', 'Mars'],
        ['Jupiter', 'Saturn', 'Uranus'],
        ['Neptune', 'Pluto', 'Moon'],
    ]


def planets_start(update, context):
    update.message.reply_text(
        "Выберите планету",
        reply_markup=ReplyKeyboardMarkup(reply_keyboards, one_time_keyboard=True)
    )
    return "planet"


def get_planet(update, context):
    print(update.message.text)
    list_word = update.message.text.title()
    for item in reply_keyboards:
        if list_word in item:
            class_planet = getattr(ephem, list_word)()
            current_time = datetime.now().strftime("%Y/%m/%d") 
            class_planet.compute(current_time)
            print(class_planet)
            update.message.reply_text(ephem.constellation(class_planet)[1], reply_markup=main_keyboard())
            return ConversationHandler.END
        continue
    else:
        update.message.reply_text("Выберите планету из представленных на клавиатуре!")
        return "planet"


def planet_dontknow(update, context):
    update.message.reply_text('Я Вас не понимаю!')
