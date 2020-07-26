FROM python:alpine3.9

RUN apk add gcc git musl-dev linux-headers openssl-dev libffi-dev

RUN mkdir /opt/test

WORKDIR /opt/test

COPY ./requirements/requirements.txt /opt/test/requirements/requirements.txt

RUN pip install -r requirements/requirements.txt

COPY . /opt/test
