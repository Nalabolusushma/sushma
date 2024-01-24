import boto3
 
cloudwatch = boto3.client('cloudwatch')
 
response = cloudwatch.put_metric_alarm(
    AlarmName='firstalaram',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=30,
    Statistic='Average',
    Threshold=70,
    ActionsEnabled=False,
    Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': 'i-070c43dc1a5ed46af'
        },
    ],
)
 
print(response)