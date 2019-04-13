#!/bin/bash
echo 'Start building resolver app'
echo 'Build resolver image'
docker build -f Dockerfile.app -t resolver .;
echo 'Build static files for front'
cd front/app
npm run build
cd ../../
echo 'Build nginx image'
docker build -f Dockerfile.nginx -t app_nginx .;
echo 'Save resolver image to *.tar file'
docker save resolver -o resolver.tar;
echo 'Save nginx image to *.tar file'
docker save app_nginx -o app_nginx.tar;
echo 'Copy and moving files'
mkdir resolver
mv resolver.tar resolver
mv app_nginx.tar resolver
cp README.rst resolver
cp docker-compose.yml resolver
cp deploy.sh resolver
echo 'Create archive with images'
tar -zcvf resolver.tar.gz resolver
rm -rf resolver
echo 'Success'