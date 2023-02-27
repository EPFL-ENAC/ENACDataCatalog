setup:
	./ensure-path.sh; python3 mount.py
run:
	docker-compose pull
	docker-compose build --parallel --no-cache
	docker-compose up -d --remove-orphans

build:
	bash rebuild.sh


stop:
	bash stop.sh


start:
	bash start.sh
