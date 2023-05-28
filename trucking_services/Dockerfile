FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install celery
RUN pip install redis
RUN pip install -U "celery[redis]"
