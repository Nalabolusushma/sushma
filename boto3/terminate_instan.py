import boto3
 
client = boto3.client('ec2')
 
response = client.terminate_instances(
    InstanceIds=[
        'i-02e51aa7f5d3ac43a ',
    ]
)