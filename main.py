# we're using PyTelegramBotApi library
from telebot import TeleBot
from environs import Env
env = Env()
env.read_env('.env')
BOT_TOKEN = env("BOT_TOKEN")
bot = TeleBot(token=BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id=chat_id, text="hi, welcome")
    
@bot.message_handler(content_types=['text'])
def start_command(message):
    chat_id = message.chat.id
    mes = message.text
    bot.send_message(chat_id=chat_id, text=mes)
    
print("polling")
bot.polling()
