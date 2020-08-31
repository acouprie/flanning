FROM python:3.8-slim

LABEL title "Flask-calendar"
LABEL maintainer "Antoine Couprie"
LABEL contrib1 "https://github.com/acouprie"

# Define environment vars to expose to container here
# ENV <key> <value>

# Env vars sent from docker-compose or docker build
#ARG uid=1000
#ARG gid=1000

#RUN getent group $gid || groupadd --gid $gid flask-calendar
#RUN getent passwd $uid || useradd -m -u $uid -g $gid flask-calendar

#RUN chown -R $uid:$gid /usr/local

#USER $uid

COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
