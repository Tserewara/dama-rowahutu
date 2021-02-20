FROM python:3.8-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

ENV POSTGRES_HOST=damarowahutu-db

ENV POSTGRES_PASSWORD=tserewara

WORKDIR damarowahutu/

COPY src/ src/

COPY requirements.txt .

COPY run.sh .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["sh", "run.sh"]