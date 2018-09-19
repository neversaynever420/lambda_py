import json
import boto3
import logging

s3 = boto3.client('s3')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # TODO implement
    bucketName = event['detail']['requestParameters']['bucketName']
    objectKey = event['detail']['requestParameters']['key']
    if objectKey.lower().endswith(('.pem', '.ppk','.jpg')):
        response = s3.delete_object(
        Bucket= bucketName,
        Key= objectKey
      )