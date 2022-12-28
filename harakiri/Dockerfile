FROM python:3.10.8-buster
LABEL maintainer="Denis Sventitsky <denis.sventitsky@gmail.com> / Twisted Fantasy <twisteeed.fantasy@gmail.com>"

RUN apt-get -y update && apt-get -y install git

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/harakiri/
RUN mkdir -p /usr/src/static/
WORKDIR /usr/src/harakiri/

COPY harakiri/ .
RUN pip --cache-dir=/usr/src/harakiri/.pip-cache install -r requirements.txt
