FROM python:slim

RUN useradd anjawebhooks

WORKDIR /home/anjawebhooks

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql cryptography

COPY app app
COPY migrations migrations
COPY app.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP microblog.py

RUN chown -R anjawebhooks:anjawebhooks ./
USER anjawebhooks

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]