# какой язык программирования
FROM python:latest

#
COPY . /code

# Назначить основную папку
WORKDIR /code

# Установка библиотек
RUN pip install uvicorn fastapi

RUN pip install telebot

CMD ["uvicorn", "main:app", "--reload"]
