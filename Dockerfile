FROM python:3.9-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /COD

COPY requirements.txt /COD/

RUN pip install -r requirements.txt
COPY . .


