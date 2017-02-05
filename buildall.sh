#! /bin/bash

docker build --no-cache -t web -f frontend
docker build --no-cache -t server -f server