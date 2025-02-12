#!/bin/bash

# Turn on bash's job control
set -m

# Collect static files in /static_root
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate

# Run Django
## For development
python manage.py runserver 0.0.0.0:8000 &
fg %1