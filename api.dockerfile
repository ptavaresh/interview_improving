# Base Image
#FROM python:3.6
FROM ubuntu:16.04


# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8000

# Install system dependencies
RUN apt-get update && apt-get install -y \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        apache2 \
        apache2-utils \
        wget \
        unzip \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/ptavaresh/travel_api/archive/master.zip
RUN unzip master.zip
RUN rm -rf master.zip

# create and set working directory
RUN mkdir /app
# Add current directory code to working directory
RUN cp -a /travel_api-master/* /app
WORKDIR /app

# install environment dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv

# Install project dependencies
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD gunicorn travel_api.wsgi:application --bind 0.0.0.0:$PORT 
