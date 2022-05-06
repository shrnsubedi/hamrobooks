FROM python:3.9-alpine

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .