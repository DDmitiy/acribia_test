#!/bin/bash
echo 'Start deploying'
echo 'Loading resolver image'
docker load -i resolver.tar;
echo 'Loading nginx image'
docker load -i app_nginx.tar;
echo 'Starting application'
docker-compose -p resolver up -d;
