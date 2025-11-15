FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# copy all project files (manage.py + offersAdmin + admin_panel etc)
COPY . /app

RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["sh", "-c", "\
    python manage.py collectstatic --noinput && \
    python manage.py migrate --noinput && \
    gunicorn --bind 0.0.0.0:8000 --workers 2 offersAdmin.wsgi:application \
"]
