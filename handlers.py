from glob import glob
from random import choice
from visa_wait_times import get_html
from calculator import calculator
from utils import get_smile, play_random_numbers, main_keyboard
from datetime import datetime
import ephem


def greet_user(update, context):
    print('Вызван /start')
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f'Здравствуй, пользователь {context.user_data["emoji"]}!',
        reply_markup = main_keyboard()
    )
    print(update.message)


def get_planet(update, context):
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
        update.message.reply_text(ephem.constellation(class_planet), reply_markup = main_keyboard())


def calculator_user(update, context):
    cal_user = update.message.text.split(' ')
    print(cal_user)
    if len(cal_user[1]) == 1:
        update.message.reply_text('Введите выражение, которое необхоимо посчитать')
    else:
        update.message.reply_text(calculator(cal_user[1]), reply_markup = main_keyboard())


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
    update.message.reply_text(message, reply_markup = main_keyboard())


def send_cat_picture(update, context):
    cat_photo_list = glob('images/*.jp*g')
    cat_photo_filename = choice(cat_photo_list)
    print(cat_photo_filename)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_photo_filename, 'rb'), reply_markup = main_keyboard())


def get_date_visa(update, context):
    user_street = update.message.text.split(' ')
    print(user_street)
    if len(user_street[1]) < 2:
        update.message.reply_text('Введите город на Англ. языке!')
    else:
        update.message.reply_text(f'Город {user_street[1]}:\n{get_html(user_street[1])}', reply_markup = main_keyboard())


def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    print(coords)
    update.message.reply_text(
        f"Ваши координаты {coords} {context.user_data['emoji']}!",
        reply_markup = main_keyboard()
    )


def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f'{text} {context.user_data["emoji"]}', reply_markup = main_keyboard())