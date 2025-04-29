#!/bin/sh
export GUNICORN_WORKERS=2 
python manage.py collectstatic --no-input
# Apply migrations
python manage.py migrate
if [[ "$ENV_STATE" == "production" ]]; then
    gunicorn --bind 0.0.0.0:8000 core.wsgi --workers ${GUNICORN_WORKERS:-2} --forwarded-allow-ips "*"
else
    python manage.py runserver 0.0.0.0:8000
fi
