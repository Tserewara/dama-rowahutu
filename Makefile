build:
	docker-compose build --no-cache --build-arg POSTGRES_PASSWORD=$(POSTGRES_PASSWORD) --build-arg SECRET_KEY=$(SECRET_KEY)

up: build
	docker-compose up -d

test: build up
	docker-compose exec -T app pytest
	make down

unit-tests: up
	docker-compose exec -T app pytest tests/unit

integration-tests: up
	docker-compose exec -T app pytest tests/integration

e2e-tests: up
	docker-compose exec -T app pytest tests/e2e

logs:
	docker-compose logs --tail=25 app

down:
	docker-compose down --remove-orphans

all: down build up test

local_test:
	docker-compose build --no-cache --build-arg POSTGRES_PASSWORD=tserewara --build-arg SECRET_KEY=tserewara
	docker-compose up -d
	docker-compose exec app pytest
