#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import dotenv

# .env file is on upper level than manage.py
dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

# If manage.py starts manually, then we set POSTGRES_HOST to localhost
# Because if manage.py starts from docker-compose, then we use daphne to run ASGI server
os.environ.update({"POSTGRES_HOST": "localhost"})


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
