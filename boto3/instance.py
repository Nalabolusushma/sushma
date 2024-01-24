import boto3

# Create an EC2 client
client = boto3.client('ec2')
# Launch the EC2 instance
response = client.run_instances(
    ImageId='ami-0c7217cdde317cfec',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
     {
         'ResourceType': 'instance',
         'Tags':[
             {
                 'Key': 'Name',
                'Value': 'sushma_instance'
             }
         ]
     }
    ]
)
