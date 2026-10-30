import sqlite3
import telebot
from telebot import types
from config import TOKEN, DATABASE
from logic import DB_Manager

bot = telebot.TeleBot(TOKEN)
manager = DB_Manager(DATABASE)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Выбрать вино ->", callback_data="get_wine")
    markup.add(btn)
    
    bot.send_message(
        message.chat.id, 
        "Привет! Я бот-вино. Нажми кнопку ниже, чтобы получить случайное вино!", 
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "get_wine")
def callback_query(call):
    wine = manager.get_random_wine()
    fixed_acidity, alcohol, quality = wine
    text = (
        "✨ **Случайное вино для вас:**\n\n"
        f"Кислотность (fixed acidity): `{fixed_acidity}`\n"
        f"Алкоголь: `{alcohol}%`\n"
        f"Оценка качества (quality): `{quality}/10`"
    )

    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Еще бокал?", callback_data="get_wine")
    markup.add(btn)

print("запущено")
bot.infinity_polling()