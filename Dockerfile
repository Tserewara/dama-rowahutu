FROM python:3.8-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

ARG POSTGRES_PASSWORD

ENV POSTGRES_HOST=damarowahutu-db

ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD

WORKDIR dama-rowahutu/

COPY src/ src/

COPY tests/ tests/

COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "src.articles.entrypoints.web_app:app"]
