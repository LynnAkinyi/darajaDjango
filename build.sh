#!/bin/bash
source venv/bin/activate
gunicorn transaction_site.wsgi:application

