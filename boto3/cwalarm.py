import json
import boto3
import csv
import io
s3_client = boto3.client('s3')
def lambda_handler(event,context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print(bucket)
    print(key)
    response = s3_client.get_object(Bucket=bucket, Key=key)
    data = response['Body'].read().decode('utf-8')
    reader = csv.reader(io.StringIO(data))
    next(reader)
    for row in reader:
        print(str.format("Year -{}, Mileage - {}, Price -{}", row[0], row[1], row[2]))