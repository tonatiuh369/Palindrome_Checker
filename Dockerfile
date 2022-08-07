# Dockerfile

FROM python:3.10-slim

COPY requirements.txt /

COPY templates/ /templates/

RUN pip3 install -r /requirements.txt

COPY main.py .

CMD ["gunicorn"  , "-b", "0.0.0.0:8888", "main:app"]