import telebot
from telebot import types
import currencies
import info

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('Валюта')
itembtn2 = types.KeyboardButton('Новости')
markup.add(itembtn1, itembtn2)

bot = telebot.TeleBot('1870745907:AAEV4rlKC4zCr8xXjkKlN0YjqLMNoqXTav4')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Добро пожаловать", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def button(message):
    chat_id = message.chat.id
    if message.text == itembtn1.text:
        bot.send_message(chat_id,info.callback())
    elif message.text == itembtn2.text:
        bot.send_message(chat_id,currencies.get())


bot.polling()