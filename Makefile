APPLICATION_NAME = mindbox_backend
DB_CONTAINER_NAME = market_db


init:
	poetry install
	poetry shell

revision:
	cd $(APPLICATION_NAME)/db && alembic revision --autogenerate

migrate:
	cd $(APPLICATION_NAME)/db && alembic upgrade head

db:
	docker-compose -f docker-compose.yml up -d && make migrate

open_db:
	docker exec -it $(DB_CONTAINER_NAME) psql -d market_db -U user

run:
	uvicorn $(APPLICATION_NAME).__main__:app --reload --port=80 --host="localhost"

test:
	poetry run python -m pytest --verbosity=2 --showlocals --log-level=DEBUG

all_services:
	docker-compose -f docker-compose.prod.yml up -d

upload_db:
	docker exec $(DB_CONTAINER_NAME) pg_dumpall -c -U user > dump.sql

restore_db:
	docker exec -i $(DB_CONTAINER_NAME) psql -d market_db -U user < dump.sql


