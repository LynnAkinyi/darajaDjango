#!/bin/bash
source /opt/render/project/src/venv/bin/activate
gunicorn transaction_site.wsgi:application