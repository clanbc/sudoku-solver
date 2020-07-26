FROM python:alpine3.9

LABEL maintainer="clanbc"

RUN apk add gcc musl-dev linux-headers openssl-dev libffi-dev

RUN mkdir /opt/code

WORKDIR /opt/code

COPY ./requirements/requirements.txt /opt/code/requirements/requirements.txt

RUN pip install -r requirements/requirements.txt

COPY . /opt/code

CMD ["python", "sudoku_solver/main.py"]
