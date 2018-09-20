import boto3
s3 = boto3.client('s3')
sns = boto3.client('sns')

def lambda_handler(event, context):
    # TODO implement
    bucketName = event['detail']['requestParameters']['bucketName']
    objectKey = event['detail']['requestParameters']['key']
    user = event['detail']['userIdentity']['userName']
    if objectKey.lower().endswith(('.pem', '.ppk')):
        sns.publish(
        TopicArn='arn:aws:sns:ap-south-1:508037994253:s3objectputNotify',
        Message="%s has uploaded a private key file %s in bucket %s" %(user, objectKey, bucketName),
        Subject='Illegal filetype upload'
    )
        response = s3.delete_object(
        Bucket= bucketName,
        Key= objectKey
      )