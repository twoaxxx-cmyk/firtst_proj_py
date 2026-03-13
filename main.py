import telebot

# ВСТАВЬ СВОЙ ТОКЕН СЮДА (между кавычками)
TOKEN = '8690493626:AAHlM3tIkEitl9k_eCRJBBKEY1QyQI_GeFM'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой первый бот и я работаю!")
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я умею отвечать на /start и повторять за тобой.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

print("✅ Бот запущен! Иди в Telegram и напиши /start")
bot.infinity_polling()