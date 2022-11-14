FROM python:latest
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /main

COPY requirements.txt /main/

RUN pip install -r requirements.txt
COPY . .


