FROM --platform=linux/x86_64 python:3.10.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update
RUN apt install -y firefox-esr
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/