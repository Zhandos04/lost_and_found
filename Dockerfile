FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "lost_and_found.wsgi:application", "--bind", "0.0.0.0:8000"]
