# -*- coding: utf-8 -*-
import telebot
from telebot import types
from logger import Logger
from time import time
from config import start_mesage, help_message
from ttoken import token
from json import dumps, loads
from sql_control import create_user_if_exist, get_sity, get_day, get_plase, get_txt_foto_audio

bot = telebot.TeleBot(token)
logger = Logger(f"logs/{round(time())}.log")


@bot.message_handler(commands=['start'])
def start_message(message):
    if create_user_if_exist(message.from_user.id):
        bot.send_message(message.from_user.id, "📀Аккаунт успешно создан)")
    logger.info(f"Start message ({message.text}) from {message.from_user.id}")
    bot.send_message(message.from_user.id, start_mesage)


@bot.message_handler(content_types=['text'], commands=['listen'])
def listen_comand_handler(message):
    logger.info(f"Get message {message.text} from {message.from_user.username}({message.from_user.id})")

    sityes = get_sity()
    markup = types.InlineKeyboardMarkup()
    for i in sityes:
        json = f"{i[0]}-_-_"
        button1 = types.InlineKeyboardButton(i[0], callback_data=json)
        markup.add(button1)
    bot.send_message(message.from_user.id, "Выбери город:", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    if create_user_if_exist(message.from_user.id):
        bot.send_message(message.from_user.id, "📀Аккаунт успешно создан)")
    logger.info(f"Get message {message.text} from {message.from_user.username}({message.from_user.id})")
    bot.send_message(message.from_user.id, help_message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    logger.info(f"Get data '{call.data}' from {call.from_user.username}({call.from_user.id})")

    data = call.data.split("-")
    logger.info(data)

    if data[0] != "_" and data[1] == "_":
        logger.info("send 2 choise")
        days = get_day(data)
        markup = types.InlineKeyboardMarkup()
        print(data)
        for i in days:
            json = f"{data[0]}-{i[0]}-_"
            button1 = types.InlineKeyboardButton(i[0], callback_data=json)
            markup.add(button1)
        bot.send_message(call.from_user.id, "Выбери день:", reply_markup=markup)
    elif data[0] != "_" and data[1] != "_" and data[2] == "_":
        logger.info("send 3 choise")
        plases = get_plase(data)
        markup = types.InlineKeyboardMarkup()
        print(data)
        for i in plases:
            json = f"{data[0]}-{data[1]}-{i[0]}"
            button1 = types.InlineKeyboardButton(i[0], callback_data=json)
            markup.add(button1)
        bot.send_message(call.from_user.id, "Выбери место:", reply_markup=markup)
    elif data[0] != "_" and data[1] != "_" and data[2] != "_":
        logger.info("send about")
        dt = get_txt_foto_audio(data)
        bot.send_message(call.from_user.id, dt[0])

        bot.send_message(call.from_user.id, "Попытка подгрузки файла")
        audio = open(f'audio/{dt[1]}', 'rb')
        bot.send_audio(call.from_user.id, audio)
        audio.close()




bot.polling(none_stop=True)
