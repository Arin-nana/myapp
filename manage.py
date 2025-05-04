#!/usr/bin/env python
"""Django’s command-line utility for administrative tasks."""
import os
import sys

def main():
    # Если settings.py лежит в этой же папке:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')    # Если вы впоследствии вынесете settings.py в подпапку myproject,
    # замените на 'myproject.settings'
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Убедитесь, что виртуальная среда активирована "
            "и Django установлено."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
