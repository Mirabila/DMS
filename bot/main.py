import telebot
import db.psql_to_xlsx
from db.psql_to_xlsx import get_xlsx
from db.xlsx_to_psql import create_table

from my_token import secrets
token = secrets.get('BOT_API_TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])


def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️")

@bot.message_handler(commands=['report'])

def report_message(message):
    get_xlsx()
    with open('data/result.xlsx', 'rb') as f1:
        bot.send_document(message.from_user.id, f1)

bot.polling(none_stop=True, interval=0)

if __name__ == "__main__":
    create_table()