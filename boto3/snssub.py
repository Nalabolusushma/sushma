import boto3

# Create an SNS client
sns = boto3.client('sns', region_name='us-east-1')

# SNS topic ARN
sns_topic_arn = 'arn:aws:sns:us-east-1:121572617256:UPIUtilization'

# Email address to subscribe
email_address = 'sushmareddyn2@gmail.com'

# Create an email subscription
sns.subscribe(
    TopicArn=sns_topic_arn,
    Protocol='email',
    Endpoint=email_address
)

print(email_address)