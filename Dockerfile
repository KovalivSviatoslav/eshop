FROM python:3.9.1-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HOME_APP=/usr/app/backend

WORKDIR $HOME_APP
EXPOSE 8000

COPY src $HOME_APP
COPY requirements.txt $HOME_APP

RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    git bash

RUN pip install -r requirements.txt