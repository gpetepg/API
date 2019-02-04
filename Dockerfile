FROM python:3.6
LABEL maintainer "Person <person@gmail.com>"
RUN apt-get update
RUN mkdir /API
WORKDIR /API
COPY . /API
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_ENV="docker"
EXPOSE 5000




