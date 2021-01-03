FROM python:3.9.1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HOME_APP=/usr/app/backend

WORKDIR $HOME_APP

COPY requirements.txt $HOME_APP
RUN pip install -r requirements.txt

COPY ./src $HOME_APP