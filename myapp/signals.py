#signals.py
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils.timezone import now
from django.urls import resolve
from .models import TelegramSubscriber
from .telegram_bot import bot

@receiver(user_logged_in)
def notify_admin_login(sender, request, user, **kwargs):
    resolver = resolve(request.path_info)
    if resolver.namespace == 'admin':
        login_time = now().strftime('%Y-%m-%d %H:%M:%S')
        text = f"Дата входа: {login_time}\nИмя пользователя: {user.username}"
        for sub in TelegramSubscriber.objects.all():
            try:
                bot.send_message(sub.chat_id, text)
            except Exception as e:
                pass
