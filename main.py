# -*- coding: utf-8 -*-
import telebot
from logger import Logger
from time import time
from config import start_mesage
from ttoken import token

bot = telebot.TeleBot(token)
logger = Logger(f"logs/{round(time())}.log")


@bot.message_handler(commands=['start'])
def start_message(message):
    logger.info(f"Start message ({message.text}) from {message.from_user.id}")
    bot.send_message(message.from_user.id, start_mesage)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    logger.info(f"Get message {message.text} from {message.from_user.username}({message.from_user.id})")
    bot.send_message(message.from_user.id, f"Вы написали: {message.text}")


bot.polling(none_stop=True)
