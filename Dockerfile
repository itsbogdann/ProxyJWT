FROM python:3.8

COPY /src/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

EXPOSE 8000

COPY ./src /app

WORKDIR /app