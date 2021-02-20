FROM postgres:13.2-alpine

ENV POSTGRES_PASSWORD=tserewara

EXPOSE 5432

COPY ./database/init.sql /docker-entrypoint-initdb.d/