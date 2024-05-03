FROM python:3.8.10

WORKDIR /app

RUN pip3 install --upgrade pip

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
