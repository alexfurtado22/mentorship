#!/bin/sh
export GUNICORN_WORKERS=2 

# Build Tailwind CSS (or your CSS pipeline)
npx tailwindcss -i ./theme/static/css/input.css -o ./theme/static/css/dist/styles.css --minify

python manage.py collectstatic --no-input

# Apply migrations
python manage.py migrate

if [ "$ENV_STATE" = "production" ]; then
    gunicorn --bind 0.0.0.0:$PORT core.wsgi --workers ${GUNICORN_WORKERS:-2} --forwarded-allow-ips "*"
else
    python manage.py runserver 0.0.0.0:8000
fi
