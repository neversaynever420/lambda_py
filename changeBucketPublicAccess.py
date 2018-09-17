import boto3

def lambda_handler(event,context):
    bucket = event['detail']['requestParameters']['bucketName']
    s3 = boto3.client('s3')
    PERMISSION = ['FULL_CONTROL', 'WRITE_ACP', 'READ_ACP', 'WRITE', 'READ']
    response = s3.get_bucket_acl(Bucket = bucket)
    bucketRead = response['Grants']
    for g in range(len(bucketRead)):
        #   print bucketRead[g]['Grantee']['Type']
        if bucketRead[g]['Grantee']['Type'] == 'Group' and bucketRead[g]['Grantee'][
            'URI'] == 'http://acs.amazonaws.com/groups/global/AllUsers':
            if bucketRead[g]['Permission'] in PERMISSION:
                s3.put_bucket_acl(
                    ACL='private',
                    Bucket= bucket
                )