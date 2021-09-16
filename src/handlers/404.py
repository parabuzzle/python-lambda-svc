import json

def main(event, context):
    
    return {
        'statusCode': 404,
        'body': json.dumps('Not Found')
    }