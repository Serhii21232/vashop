import os
import telebot

TOKEN = os.getenv("TOKEN")

CHANNEL_LINK = "https://t.me/+U0SUWivTGNM2NzQ6"
FUNPAY_LINK = "https://funpay.com/users/14346017/"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    username = message.from_user.first_name

    bot.send_message(
        message.chat.id,
        f"👋 Привет, {username}! Добро пожаловать в 💨 VAPE PLUG📉!\n\n"
        f"Надоело переплачивать за аренду и наценки обычных магазинов?\n"
        f"Мы закупаем товар напрямую большими партиями и делимся выгодой с тобой.\n\n"
        f"🔥 Продажа по низу рынка!\n"
        f"Лучшие цены на:\n"
        f"— Вейпы\n"
        f"— Поды\n"
        f"— Жижи\n"
        f"— Одноразки\n\n"
        f"📢 Официальная ссылка на канал:\n{CHANNEL_LINK}\n\n"
        f"#Иркутск #Вейп #Жижа #ПродажаВейпов #КупитьПод #КупитьЖижу\n\n"
        f"🤖 Бот сделан warilidi\n"
        f"💬 По поводу заказа писать на FunPay:\n{FUNPAY_LINK}"
    )


@bot.message_handler(func=lambda m: m.text and m.text.lower() in [
    "привет",
    "здравствуйте",
    "hello",
    "hi"
])
def hello_message(message):
    username = message.from_user.first_name

    bot.send_message(
        message.chat.id,
        f"👋 Привет, {username}!\n\n"
        f"📢 Официальная ссылка на канал:\n{CHANNEL_LINK}\n\n"
        f"#Иркутск #Вейп #Жижа #ПродажаВейпов #КупитьПод #КупитьЖижу"
    )


print("BOT STARTED")

bot.infinity_polling(skip_pending=True)
