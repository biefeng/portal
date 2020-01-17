FROM python:2.7-alpin3.10
WORKDIR /home/BieFeNg/workspace/portal

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install uwsgi

COPY portal portal
COPY migrations migrations
COPY test.db test.db

RUN venv/bin/flask db upgrade

CMD ["flask","run"]