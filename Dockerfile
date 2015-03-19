FROM python:2.7

ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt
EXPOSE 8000

CMD python logtutum.py
