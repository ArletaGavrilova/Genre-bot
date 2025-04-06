from logic import DB_Manager
from config import *
from telebot import TeleBot

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Я бот по узнавании твоего жанра песен!) 
""")

    
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling()