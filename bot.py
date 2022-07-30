import telebot
from generator import generate_coupon

bot = telebot.TeleBot("REDACTED")

@bot.message_handler(content_types=['text'])
def started(message):
    bot.send_message(message.chat.id, f"Купон: {generate_coupon()}\nСрок действия - 7 дней")

bot.polling()