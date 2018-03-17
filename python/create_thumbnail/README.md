# Automatically create thumbnails

This serverless function will automatically create a thumbnail version of an image in S3 in a new bucket.

## Build

```
docker run -it -v "$PWD":/home python:3.6.4-jessie bash
pip install virtualenv
virtualenv ./thumbnails
source ./thumbnails/bin/activate
pip install Pillow
pip install boto3
cd ./thumbnails/lib/python3.6/site-packages
zip -r9 /home/thumbnails.zip *
cd /home
zip -g create_thumbnails.py thumbnails.zip
```
