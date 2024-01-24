import boto3
s3_client = boto3.client('s3')
def lambda_handler(event,context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print(bucket)
    print(key)
    response = s3_client.get_object(Bucket=bucket, Key=key)
