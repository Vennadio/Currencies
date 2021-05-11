import telebot;
bot = telebot.TeleBot('1587022095:AAGxxj3yrqsnDmMiB32-Y7rsVk-Ae-vLtg4')
@bot.message_handler(content_types=['text', 'document', 'audio'])
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Шалом Алейхем")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Ты еврей или гой?")
    elif message.text == 'Еврей':
        bot.send_message(message.from_user.id, "Хава Нагила!")
    elif message.text == 'Гой':
        bot.send_message(message.from_user.id, "Пиздуй отсюда")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)
