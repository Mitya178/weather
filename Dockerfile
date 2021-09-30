

FROM python:3.7-alpine

MAINTAINER Dmitriy Voronkov 'voronkov.vot@yandex.ru'

WORKDIR /opt/Devops_school/my_Flask_app

COPY . .

RUN python3 -m pip install -r requirements.txt





CMD ["python3", "main.py"]
