# Automatically create thumbnails

This serverless function will automatically create a thumbnail version of an image in S3 in a new bucket.

## Build

```
docker run -it -v "$PWD":/home python:3.6.4-jessie bash
./home/build_zip.sh
```
