#!/bin/bash
source /Users/lynnakinyi/Desktop/DarajaAPI/venv/bin/activate
gunicorn transaction_site.wsgi:application

