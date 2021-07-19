DOCKER_COMPOSE_YAML = docker-compose.yml
PROXY_CONTAINER = proxyjwt
HTTP_PORT = 8000

build:
	docker-compose build $(PROXY_CONTAINER)

run:
	docker-compose run -p $(HTTP_PORT) $(PROXY_CONTAINER)

run_background:
	docker-compose run -p $(HTTP_PORT) -d $(PROXY_CONTAINER)

down:
	docker-compose down

test:
	pytest

test_with_printing:
	pytest -rP
