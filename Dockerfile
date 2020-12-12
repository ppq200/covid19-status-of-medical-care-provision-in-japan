FROM python:3.8-slim

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

RUN groupadd -r app && \
    useradd -r -g app app

USER app

COPY . /app
WORKDIR /app

ENV FLASK_APP "main.py"

CMD ["./entrypoint.sh"]
