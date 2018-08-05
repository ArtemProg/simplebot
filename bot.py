# -*- coding: utf-8 -*-

# Для работы с телеграм ботом и прокси ставим пакеты
# pip install python-telegram-bot
# pip install python-telegram-bot[socks]

import settings
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# Updater - это компонент отвечающий за комутацию с сервером
# Telegram - именно он получает/передает сообщения
# CommandHandler - обработчика комманд, подписка на событие
# MessageHandler - обработчик для работы с обычными сообщениями

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log')

def start_bott(bot, updater):
    # print(updater)
    updater.message.reply_text('Hello {name}'.format(name=updater.message.from_user.last_name))

def chat(bot, updater):
    text = updater.message.text
    logging.info(text)
    updater.message.reply_text(text)

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():

    # Настройки прокси
    REQUEST_KWARGS = {'proxy_url': 'socks5://{ip}:{port}'.format(ip=settings.PROXY_IP, port=settings.PROXY_PORT),
        # Optional, if you need authentication:
        'urllib3_proxy_kwargs': {'username': '', 'password': ''}}

    updtr = Updater(settings.TOKEN, request_kwargs=REQUEST_KWARGS)
    
    updtr.dispatcher.add_handler(CommandHandler('start', start_bott))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updtr.start_polling()
    updtr.idle()

if __name__ == '__main__':
    logging.info('Bot started')
    main()



# # -*- coding: utf-8 -*-
# from telegram.ext import Updater         # пакет называется python-telegram-bot, но Python-
# from telegram.ext import CommandHandler  # модуль почему-то просто telegram ¯\_(ツ)_/¯

# def start(bot, update):
#     # подробнее об объекте update: https://core.telegram.org/bots/api#update
#     bot.sendMessage(chat_id=update.message.chat_id, text="Здравствуйте.")

# updater = Updater(token='678012631:AAHm3QfALJ3qwE4l5t1ZFtCgx5vdDj5ViNU')  # тут токен, который выдал вам Ботский Отец!

# start_handler = CommandHandler('start', start)  # этот обработчик реагирует
#                                                 # только на команду /start

# updater.dispatcher.add_handler(start_handler)   # регистрируем в госреестре обработчиков
# updater.start_polling()  # поехали!
# updater.idle()