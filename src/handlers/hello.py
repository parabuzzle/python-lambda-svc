import json

from src.lib import get_query_parameter_value, get_path_parameter_value

def main(event, context):
    salutation = get_query_parameter_value(event, 'salutation')
    name = get_path_parameter_value(event, 'name')

    if salutation is None:
        salutation = 'Hello'
    
    if name is None:
        name = 'World'

    response = salutation + ' ' + name
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
