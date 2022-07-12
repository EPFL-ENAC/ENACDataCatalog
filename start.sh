#!/bin/bash
docker-compose build && docker-compose up -d
http-server /mnt/harvest/meteosuisse

