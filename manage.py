#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\dmr\\PycharmProjects\\django_game', 'C:/Users/dmr/PycharmProjects/django_game'])
sys.path.extend(['/Users/alisaidomar/Downloads/django_game'])

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mygame.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
