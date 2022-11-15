FROM python:3.9-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /main

COPY requirements.txt /main/

RUN pip install -r requirements.txt
COPY . .


