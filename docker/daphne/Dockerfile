
FROM python:3.8
MAINTAINER Mikhail Gumen

ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY .env .env
RUN pip install -r requirements.txt
ENV DJANGO_SETTINGS_MODULE=keyua_asgi_app.settings
ENTRYPOINT ["/usr/src/app/docker/daphne/entrypoint.sh"]