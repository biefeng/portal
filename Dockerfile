FROM python:2.7.17-buster
WORKDIR /home/BieFeNg/workspace/portal

COPY requirements.txt requirements.txt
#RUN python -m venv venv
#RUN venv/bin/pip install -r requirements.txt
#RUN venv/bin/pip install uwsgi
ENV FLASK_APP portal
RUN pip install -r requirements.txt
RUN pip install uwsgi

COPY portal portal
COPY migrations migrations
COPY test.db test.db
COPY uwsgi.ini uwsgi.ini
COPY wsgi.py wsgi.py

#RUN flask db upgrade

CMD ["uwsgi","--ini","uwsgi.ini"]