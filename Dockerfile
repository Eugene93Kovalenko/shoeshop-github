FROM python:3.11.4-slim-buster
MAINTAINER Eugene Kovalenko, keugenemail@gmail.com

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY shoeshop_project /app

EXPOSE 8000

#CMD python manage.py runserver 8000