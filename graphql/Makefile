DC = docker-compose -f docker-compose.yml -p shopping-list
ALEMBIC_PATH = ./api/migrations

up:
	$(DC) up

stop:
	$(DC) stop

makemigrations:
	$(DC) exec api alembic revision --autogenerate -m "$(filter-out $@,$(MAKECMDGOALS))"

migrate:
	$(DC) exec api alembic upgrade head

up-db:
	$(DC) up -d database

delete-db: stop
	$(DC) rm -v database
	rm -rf $(ALEMBIC_PATH)/versions/*

recreate-db: delete-db up
	sleep 2
	$(MAKE) makemigrations "init"
	$(MAKE) migrate

%:
	@: