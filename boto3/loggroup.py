import boto3
cloudwatch_logs = boto3.client('logs', region_name='us-east-1')
log_group_name = 'MyLog1'
cloudwatch_logs.create_log_group(
    logGroupName=log_group_name
)

print(log_group_name)
