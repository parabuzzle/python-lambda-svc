import os
import json

from ..lib import query_parameters, path_parameters

def main(event, context):

    response = {
        'queryParameters': query_parameters(event),
        'pathParameters': path_parameters(event),
        'aws': {
            'region': os.environ['AWS_REGION'],
            'default region': os.environ['AWS_DEFAULT_REGION'],
            'function name': os.environ['AWS_LAMBDA_FUNCTION_NAME'],
            'function version': os.environ['AWS_LAMBDA_FUNCTION_VERSION'],
            'function memory size': os.environ['AWS_LAMBDA_FUNCTION_MEMORY_SIZE'],
            'log group': os.environ['AWS_LAMBDA_LOG_GROUP_NAME'],
            'log stream': os.environ['AWS_LAMBDA_LOG_STREAM_NAME'],
            
        },
        'event': event,
        'environment': dict(os.environ),
        'context': {
            'Lambda function ARN': context.invoked_function_arn,
            'CloudWatch log stream name': context.log_stream_name,
            'CloudWatch log group name': context.log_group_name,
            'Lambda Request ID': context.aws_request_id,
            'Lambda function memory limits in MB': context.memory_limit_in_mb,
            'Lambda time remaining in MS': context.get_remaining_time_in_millis(),
        },
    }
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }