#!/bin/bash
# Exit immediately if any command fails
set -e

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn  # Ensure gunicorn is installed

# Collect static files (if using Django)
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate

# Start the application (this line might belong in your start command instead)
# gunicorn transaction_site.wsgi:application