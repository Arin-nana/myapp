# myapp/tests/test_signals.py
import pytest
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.test import RequestFactory
from django.utils.timezone import now
from myapp.models import TelegramSubscriber
from myapp.signals import notify_admin_login

@pytest.mark.django_db
def test_notify_admin_login_sends_messages(mocker):
    # Создаём одного подписчика
    sub = TelegramSubscriber.objects.create(chat_id=12345)

    # Мокаем метод send_message
    bot_send = mocker.patch('myapp.signals.bot.send_message')

    # Создаём фейковый запрос в /admin/
    rf = RequestFactory()
    request = rf.get('/admin/login/')
    request.path_info = '/admin/'

    # Пользователь
    user = User.objects.create_user(username='ivan', password='pass')

    # Отправляем сигнал
    user_logged_in.send(sender=User, request=request, user=user)

    # Проверяем, что отправили именно один месседж с нужным форматом
    assert bot_send.call_count == 1
    args, _ = bot_send.call_args
    assert args[0] == sub.chat_id
    assert 'Имя пользователя: ivan' in args[1]
    assert 'Дата входа:' in args[1]
