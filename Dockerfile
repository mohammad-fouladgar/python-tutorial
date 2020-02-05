# Python 3.8.1

FROM python:3.8.1-alpine3.10

LABEL maintainer="Fouladgar dev <fouladgar.dev@gmail.com>"

COPY requirements.txt /

RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

COPY ./src /app

WORKDIR /app 

CMD [ "python" , "main.py"]