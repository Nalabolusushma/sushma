import boto3

# Create a CloudWatch client
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

# Define your alarm parameters
alarm_name = 'MyMetricAlarm'
namespace = 'MyCustomNamespace'
metric_name = 'MyCustomMetric'
threshold = 20.0  # Replace with your threshold value
comparison_operator = 'GreaterThanThreshold' 
evaluation_periods = 1
period = 60  # in seconds
statistic = 'SampleCount' 
alarm_description = 'My Metric Alarm is greater than 20%'
alarm_actions = ['arn:aws:sns:us-east-1:121572617256:UPIUtilization'] 

# Create the alarm
cloudwatch.put_metric_alarm(
    AlarmName=alarm_name,
    ComparisonOperator=comparison_operator,
    EvaluationPeriods=evaluation_periods,
    MetricName=metric_name,
    Namespace=namespace,
    Period=period,
    Statistic=statistic,
    Threshold=threshold,
    AlarmDescription=alarm_description,
    AlarmActions=alarm_actions,
    Dimensions=[{'Name': 'InstanceId', 'Value': 'i-0e8f9b10cc63e5187'}] 
)

print(alarm_name)