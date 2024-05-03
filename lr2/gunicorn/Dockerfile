FROM python:3.8.10


RUN pip3 install --upgrade pip

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8086", "--workers=2", "app:app"]