import logging
from wsgiref.handlers import format_date_time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot.log', format='%(asctime)s - %(message)s', level=logging.INFO)

# PROXY = {'proxy_url': settings.PROXY_URL,
#     'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, contex):
    print('Вызван /start')
    update.message.reply_text('Здравствуй, пользователь!')
    print(update.message)

def talk_to_me(update, contex):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True) # request_kwargs=PROXY

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot started")

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
