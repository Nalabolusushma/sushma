import boto3

cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
namespace = 'MyCustomNamespace'
metric_name = 'MyCustomMetric'
dimensions = [
    {
        'Name': 'InstanceId',
        'Value': 'i-0e8f9b10cc63e5187'  # Replace with the instance ID you want to monitor
    }
]
metric_data = [
    {
        'MetricName': metric_name,
        'Dimensions': dimensions,
        'Value': 42.0,  # Replace with your data point value
        'Unit': 'Count'  # Use an appropriate unit here
    }
]

cloudwatch.put_metric_data(
    Namespace=namespace,
    MetricData=metric_data
)