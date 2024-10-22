import boto3
import os
import sys
import uuid
from PIL import Image
import PIL.Image

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

size = 384, 384

def resize_image(image_path, resized_path):
  with Image.open(image_path) as image:
    old_size = image.size
    image.thumbnail(size, Image.ANTIALIAS)
    image.save(resized_path)
    return old_size

def handler(event, context):
  for record in event['Records']:
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']
    id = '{}{}'.format(uuid.uuid4(), key.split('/')[-1])
    download_path = '/tmp/{}'.format(id)
    upload_path = '/tmp/resized-{}'.format(id)

    s3_client.download_file(bucket, key, download_path)
    width, height = resize_image(download_path, upload_path)

    original = s3_resource.Object(bucket, key)

    original.metadata.update({
      'width': str(width),
      'height': str(height)
    })

    original.copy_from(
      CopySource={'Bucket': bucket, 'Key': key},
      Metadata=original.metadata,
      MetadataDirective='REPLACE'
    )

    s3_client.upload_file(upload_path, '{}-thumbnails'.format(bucket), key)
