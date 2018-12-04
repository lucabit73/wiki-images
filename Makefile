PROJECT=wiki-images

.PHONY: info
info:
	@echo "yo"

.PHONY: up
up:
	docker-compose --project-name=$(PROJECT) up

.PHONY: bash
bash:
	docker-compose --project-name=$(PROJECT) run django sh

.PHONY: setup
setup: migrate

.PHONY: migrate
migrate:
	docker-compose --project-name=$(PROJECT) run django python manage.py migrate