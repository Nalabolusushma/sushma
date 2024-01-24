import boto3

# Create an SNS client
sns = boto3.client('sns', region_name='us-east-1')

# Create an SNS topic
response = sns.create_topic(Name='UPIUtilization')

# Get the ARN of the created SNS topic
sns_topic_arn = response['TopicArn']

print(sns_topic_arn)