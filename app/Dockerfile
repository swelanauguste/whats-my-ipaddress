# Base Image
FROM python:3.9.6-alpine

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install environment dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements/prod.txt

EXPOSE 8000

CMD gunicorn cf.wsgi:application --bind 0.0.0.0:8000
