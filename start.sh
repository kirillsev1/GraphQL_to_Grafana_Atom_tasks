#!/bin/bash
docker volume create --name=grafana_data
docker-compose build
docker-compose up
