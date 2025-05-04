#!/usr/bin/env python
import os
import sys

def main():
    # поскольку settings.py лежит рядом с этим файлом,
    # импортируем просто 'settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Убедитесь, что оно установлено "
            "и активна виртуальная среда."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
