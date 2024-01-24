import boto3

# Create an AWS Lambda client
lambda_client = boto3.client('lambda')

# Define the Lambda function configuration
function_name = 'MyLambdaFunction'
runtime = 'python3.12'
handler = 'lambda_function.handler'
role_arn = 'arn:aws:iam::123456789012:role/lambda-execution-role'
code_zip_path = '/path/to/your/code.zip'

# Create the Lambda function
response = lambda_client.create_function(
    FunctionName=function_name,
    Runtime=runtime,
    Role=role_arn,
    Handler=handler,
    Code={
        'ZipFile': open(code_zip_path, 'rb').read()
    }
)

# Print the ARN of the created Lambda function
print(f"Lambda Function ARN: {response['FunctionArn']}")
