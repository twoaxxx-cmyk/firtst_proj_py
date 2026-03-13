import telebot
import random

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
    help_text += "/joke - случайная шутка\n"
    help_text += "/time - текущее время\n"
    help_text += "Напиши 'Привет' или 'Пока'\n"
    help_text += "Или отправь пример: 2+3"
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['joke'])
def send_joke(message):
    jokes = [
        "Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 == Dec 25!",
        "Сколько программистов нужно, чтобы поменять лампочку? Ни одного, это проблема железа.",
        "99 маленьких багов в коде, 99 маленьких багов. Исправишь один, компилируешь — 199 маленьких багов в коде.",
        "Встречаются два друга-программиста. Один говорит: — Я вчера купил себе новую клавиатуру. — А старая сломалась? — Да нет, просто я перешёл на тёмную тему и белые буквы перестал видеть."
    ]
    joke = random.choice(jokes)
    bot.reply_to(message, joke)

print("✅ Бот запущен! Иди в Telegram и напиши /start")
bot.infinity_polling()