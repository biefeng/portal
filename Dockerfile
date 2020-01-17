FROM python:2.7.17-buster
WORKDIR /home/BieFeNg/workspace/portal

COPY requirements.txt requirements.txt
#RUN python -m venv venv
#RUN venv/bin/pip install -r requirements.txt
#RUN venv/bin/pip install uwsgi
ENV FLASK_APP app
RUN pip install -r requirements.txt
RUN pip install uwsgi

COPY portal portal
COPY migrations migrations
COPY test.db test.db

RUN flask db upgrade

CMD ["flask","run"]