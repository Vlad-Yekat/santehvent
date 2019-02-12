FROM python:3.6.6
MAINTAINER Vlad Rybin <vladislavi DOG mail.ru>
ADD . /santehvent
ENV DJANGO_SETTINGS_MODULE santehvent.settings
RUN pip install -r /santehvent/requirements.txt

CMD python /santehvent/manage.py runserver 0.0.0.0:8080