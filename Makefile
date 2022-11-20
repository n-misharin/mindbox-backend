APPLICATION_NAME = mindbox_backend
DB_CONTAINER_NAME = market_db

db:
	docker-compose up -d

revision:
	cd $(APPLICATION_NAME)/db && alembic revision --autogenerate

migrate:
	cd $(APPLICATION_NAME)/db && alembic upgrade head

open_db:
	docker exec -it $(DB_CONTAINER_NAME) psql -d market_db -U user

run:
	uvicorn $(APPLICATION_NAME).__main__:app --reload --port=8000

test:
	poetry run python -m pytest --verbosity=2 --showlocals --log-level=DEBUG
