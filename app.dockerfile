FROM python:3.8

WORKDIR /app

RUN pip install redis

COPY . /app/

CMD ["python", "/app/sentinel.py"]
