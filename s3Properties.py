
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
# TODO implement
bucket = 'Your Bucket Name'

try:
  data = s3.get_bucket_encryption(Bucket=bucket)
  if len(data)>0:
   # print ("Value Present")
   data = s3.get_bucket_encryption(Bucket=bucket)
   sseAlgorithm = data['ServerSideEncryptionConfiguration']['Rules'][0]['ApplyServerSideEncryptionByDefault'][
       'SSEAlgorithm']
   if sseAlgorithm == 'AES256':
       # changeEncryption
       s3.put_bucket_encryption(Bucket=bucket, ServerSideEncryptionConfiguration={'Rules': [
           {
               'ApplyServerSideEncryptionByDefault': {
                   'SSEAlgorithm': 'aws:kms'
               }
           },
       ]})

except ClientError as e:
  # Bucket has no Default encryption Change it to AWS-KMS
    # changeEncryption
    s3.put_bucket_encryption(Bucket=bucket, ServerSideEncryptionConfiguration={'Rules': [
        {
            'ApplyServerSideEncryptionByDefault': {
                'SSEAlgorithm': 'aws:kms'
            }
        },
    ]})
