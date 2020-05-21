FROM python:3.8.2-alpine

COPY requirements.txt ./resume-api/
WORKDIR /resume-api

RUN pip install -r requirements.txt

RUN pip freeze
