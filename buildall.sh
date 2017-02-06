#! /bin/bash

docker build frontend -t web --no-cache
docker build server -t server --no-cache