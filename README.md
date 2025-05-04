# MyApp: Уведомления о входе в админку через Telegram

## Описание

`myapp` — это Django-приложение, которое отправляет уведомления в Telegram всем подписчикам сразу после успешного входа любого пользователя в административную панель Django.

При помощи сигнала `user_logged_in` и бота на `pyTelegramBotAPI` проект:

* хранит подписанные чаты в модели `TelegramSubscriber`
* отлавливает логины в `/admin/`
* рассылает сообщение с датой и именем пользователя
* покрыт автоматическими тестами для проверки рассылки

## Требования

* Python 3.10+
* Django 4.x
* pyTelegramBotAPI
* pytest и pytest-django (или встроенный unittest)
* python-dotenv (рекомендуется для `.env`)
* Токен Telegram-бота (формат `<bot_id>:<token>`, например `123456789:ABCDEF...`)

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/Arin-nana/myapp.git
   cd myapp
   ```
2. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   # Windows PowerShell
   venv\Scripts\Activate.ps1
   # Linux/macOS
   source venv/bin/activate
   ```
3. Установите зависимости из `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Конфигурация

1. Создайте файл `.env` в корне проекта рядом с `manage.py` и добавьте:

   ```ini
   TELEGRAM_TOKEN=123456789:ABCDEF-your-token-here
   ```
2. Убедитесь, что в `myproject/settings.py` подключены:

   ```python
   import os
   from pathlib import Path

   BASE_DIR = Path(__file__).resolve().parent.parent

   # ... другие настройки Django ...

   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',

       'myapp.apps.MyAppConfig',
   ]

   TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
   ```

## Применение миграций

```bash
python manage.py migrate
```

## Запуск

1. Запустите сервер Django:

   ```bash
   python manage.py runserver
   ```
2. Запустите бота (Telegram polling):

   ```bash
   python -c "import myapp.telegram_bot as tb; tb.run_polling()"
   ```

## Использование

1. В Telegram найдите вашего бота и отправьте команду `/start` — вы подпишетесь на уведомления.
2. Перейдите в `http://localhost:8000/admin/` и выполните вход под любым пользователем.
3. В чатах-подписках придёт сообщение:

   ```text
   Дата входа: 2025-05-04 14:23:10
   Имя пользователя: ivan
   ```

## Тестирование

### Django Test Runner

```bash
python manage.py test myapp
```

### Pytest + pytest-django

1. Установите:

   ```bash
   pip install pytest pytest-django
   ```
2. Создайте `pytest.ini` в корне:

   ```ini
   [pytest]
   DJANGO_SETTINGS_MODULE = myproject.settings
   python_files = tests.py test_*.py *_tests.py
   ```
3. Запустите:

   ```bash
   pytest
   ```

## Структура проекта

```
myapp/                       # корневая папка репозитория
├ manage.py                  # CLI Django
├ requirements.txt           # зависимости
├ .env.example               # образец env-файла
├ myproject/                 # пакет настроек Django
│  ├ __init__.py
│  ├ settings.py
│  ├ urls.py
│  └ wsgi.py
└ myapp/                     # приложение с ботом и сигналами
   ├ __init__.py
   ├ apps.py
   ├ models.py
   ├ signals.py
   ├ telegram_bot.py
   └ tests/                   # тесты
      ├ __init__.py
      └ test_signals.py
```

##
