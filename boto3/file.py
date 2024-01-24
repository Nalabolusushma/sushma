import boto3
 
# Create an S3 client  
s3_client = boto3.client('s3')
response = s3_client.upload_file( r'C:\Users\DELL\Documents\boto3.txt',
                                 'suchireddy-1',
                                 'boto3.txt')