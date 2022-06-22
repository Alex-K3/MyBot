from glob import glob
import os
from random import choice
from tkinter import image_names
from wait_visa import city
from calculator import calculator
from utils import play_random_numbers, main_keyboard, has_object_on_image, cat_rating_inline_keyboard
from datetime import datetime
from db import db, get_or_create_user, save_cat_image_vote, user_voted, get_image_rating
import ephem


def greet_user(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    print('Вызван /start')
    update.message.reply_text(
        f'Здравствуй, пользователь {user["emoji"]}!',
        reply_markup=main_keyboard()
    )
    print(update.message)


def get_planet(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
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
        update.message.reply_text(ephem.constellation(class_planet), reply_markup=main_keyboard())


def calculator_user(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    cal_user = update.message.text.split(' ')
    print(cal_user)
    if len(cal_user[1]) == 1:
        update.message.reply_text('Введите выражение, которое необхоимо посчитать')
    else:
        update.message.reply_text(calculator(cal_user[1]), reply_markup=main_keyboard())


def guess_number(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message = 'Введи число'
    print(context.args)
    update.message.reply_text(message, reply_markup=main_keyboard())


def send_cat_picture(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    cat_photo_list = glob('images/*.jp*g')
    cat_photo_filename = choice(cat_photo_list).replace('\\', '/')
    print(cat_photo_filename)
    chat_id = update.effective_chat.id
    if user_voted(db, cat_photo_filename, user['user_id']):
        rating = get_image_rating(db, cat_photo_filename)
        caption = f"Рейтинг картинки: {rating}"
        keyboard = None
    else:
        keyboard = cat_rating_inline_keyboard(cat_photo_filename)
        caption = None
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_photo_filename, 'rb'), reply_markup=keyboard, caption=caption)


def get_date_visa(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    user_name_city = update.message.text.split(' ')
    user_name_city[1] = str(user_name_city[1]).title()
    print(user_name_city[1])
    update.message.reply_text(city(user_name_city[1]))


def user_coordinates(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    coords = update.message.location
    print(coords)
    update.message.reply_text(
        f"Ваши координаты {coords} {user['emoji']}!",
        reply_markup=main_keyboard()
    )


def talk_to_me(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    text = update.message.text
    print(text)
    update.message.reply_text(f'{text} {user["emoji"]}', reply_markup=main_keyboard())


def check_user_photo(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    update.message.reply_text("Обрабатываю фото")
    os.makedirs('downloads', exist_ok=True)
    photo_file = context.bot.getFile(update.message.photo[-1].file_id)
    filename = os.path.join('downloads', f'{photo_file.file_id}.jpg')
    photo_file.download(filename)
    update.message.reply_text("Файл сохранен")
    if has_object_on_image(filename, object_name='cat'):
        update.message.reply_text("Обнаружен котик, добавляю в библиотеку.")
        new_filename = os.path.join('images', f'cat_{photo_file.file_id}.jpg')
        os.rename(filename, new_filename)
    else:
        os.remove(filename)
        update.message.reply_text("Тревога, котик не обнаружен!")


def cat_picture_raiting(update, context):
    update.callback_query.answer()
    callback_type, image_name, vote = update.callback_query.data.split("|")
    vote = int(vote)
    user = get_or_create_user(db, update.effective_user, update.effective_chat.id)
    save_cat_image_vote(db, user, image_name, vote)
    rating = get_image_rating(db, image_name)
    update.callback_query.edit_message_caption(caption=f"Рейтинг картинки: {rating}")   
