import telegram
import telegram.ext
import os
import telebot
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['hi'])
def say_hi(message):
    bot.reply_to(message, 'hi bdksajdlkajsd')
    
@bot.message_handler(commands=['login'])
def login(message):
    bot.send_message(message.chat.id, 'Esme tokhmito bezn:')
    bot.user.id
    bot.send_message(message.chat.id, 'logged in')
    
bot.polling()    
    