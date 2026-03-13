import telebot

# ВСТАВЬ СВОЙ ТОКЕН СЮДА (между кавычками)
TOKEN = '8690493626:AAHlM3tIkEitl9k_eCRJBBKEY1QyQI_GeFM'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой первый бот и я работаю!")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "Я умею:\n"
    help_text += "/start - приветствие\n"
    help_text += "/help - список команд\n"
    help_text += "Напиши 'Привет' или 'Пока'\n"
    help_text += "Или отправь пример: 2+3"
    bot.reply_to(message, help_text)

print("✅ Бот запущен! Иди в Telegram и напиши /start")
bot.infinity_polling()