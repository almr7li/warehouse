FROM python:3.12.1-slim

WORKDIR /app
COPY  . /app

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV DB_HOST=host.docker.internal

EXPOSE 8000
EXPOSE 5433

CMD python manage.py runserver 0.0.0.0:8000