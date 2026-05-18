import os
import telebot

TOKEN = os.getenv("8101017025:AAFwBf6aFZoxt3ymLNlZPSAFYwhZ8dla3qo")

CHANNEL_LINK = "https://t.me/+U0SUWivTGNM2NzQ6"
FUNPAY_LINK = "https://funpay.com/users/14346017/"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    username = message.from_user.first_name

    bot.send_message(
        message.chat.id,
        f"Привет, {username}!\n\n"
        f"Вот официальная ссылка на канал:\n{CHANNEL_LINK}\n\n"
        f"🤖 Бот сделан warilidi\n"
        f"По поводу заказа писать на FunPay:\n{FUNPAY_LINK}"
    )


@bot.message_handler(func=lambda message: message.text and message.text.lower() in [
    "привет",
    "здравствуйте",
    "hello",
    "hi"
])
def hello_message(message):
    username = message.from_user.first_name

    bot.send_message(
        message.chat.id,
        f"Привет, {username}!\n\n"
        f"Вот официальная ссылка на канал:\n{CHANNEL_LINK}\n\n"
        f"🤖 Бот сделан warilidi\n"
        f"По поводу заказа писать на FunPay:\n{FUNPAY_LINK}"
    )


print("Бот запущен...")
bot.infinity_polling()
