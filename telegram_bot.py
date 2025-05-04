import telebot
from django.conf import settings
from .models import TelegramSubscriber

bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    subscriber, created = TelegramSubscriber.objects.get_or_create(chat_id=chat_id)
    if created:
        bot.send_message(chat_id, "✅ Вы подписались на уведомления об входах в админку.")
    else:
        bot.send_message(chat_id, "ℹ️ Вы уже подписаны.")

def run_polling():
    bot.infinity_polling()
