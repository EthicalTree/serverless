#!/bin/bash

apt update && apt-get -y install zip
pip install virtualenv
virtualenv ./thumbnails
source ./thumbnails/bin/activate
pip install Pillow
pip install boto3
cd ./thumbnails/lib/python3.6/site-packages
zip -r9 /home/thumbnails.zip *
cd /home
zip -g thumbnails.zip create_thumbnail.py
