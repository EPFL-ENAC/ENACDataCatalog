run:
	python3 /opt/ENACDataCatalog/mount.py
	cd /opt/ENACDataCatalog; docker-compose build && docker-compose up -d

build:
	bash rebuild.sh


stop:
	bash stop.sh


start:
	bash start.sh
