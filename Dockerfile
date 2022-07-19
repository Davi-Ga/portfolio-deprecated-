FROM python:3.8.13-alpine3.15

WORKDIR /app

COPY ./src /app
COPY ./requirements.txt requirements.txt

EXPOSE 8080

RUN pip install --no-cache-dir -r requirements.txt

CMD gunicorn app:app