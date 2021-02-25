build:
	docker-compose build --build-arg POSTGRES_PASSWORD=$(POSTGRES_PASSWORD)

up: build
	docker-compose up -d

test: build up
	docker-compose exec -T app pytest

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