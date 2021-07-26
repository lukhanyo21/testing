FROM python:3.7-alpine
MAINTAINER Lukhanyo

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
RUN mkdir /src
WORKDIR /src
COPY ./src/ /src

RUN adduser -D user
USER user