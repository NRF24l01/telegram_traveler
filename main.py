# -*- coding: utf-8 -*-
import telebot
from telebot import types
from logger import Logger
from time import time
from config import start_mesage
from ttoken import token
from sql_control import create_user_if_exist, get_sity

bot = telebot.TeleBot(token)
logger = Logger(f"logs/{round(time())}.log")

@bot.message_handler(commands=['start'])
def start_message(message):
    logger.info(f"Start message ({message.text}) from {message.from_user.id}")
    bot.send_message(message.from_user.id, start_mesage)

@bot.message_handler(content_types=['text'])
def text_handler(message):
    if create_user_if_exist(message.from_user.id):
        bot.send_message(message.from_user.id, "📀Аккаунт успешно создан)")
    sitis = get_sity()
    logger.info(f"Get message {message.text} from {message.from_user.username}({message.from_user.id})")
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    for i in sitis:
        keyboard.add(types.InlineKeyboardButton(text=i, callback_data = i))
    bot.send_message(message.from_user.id, f"Вы написали: {message.text}", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data:
        print(call.data)

bot.polling(none_stop=True)
