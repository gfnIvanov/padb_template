# syntax=docker/dockerfile:1
   
# pull official base image
FROM python:3.11.3-slim-buster

# set work directory
WORKDIR /app

# copy project
COPY . .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt