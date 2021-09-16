'''
parameters parsing helpers for query parameters and path parameters
'''


def query_parameters(event):
    '''
      Function to handle getting query parameters out of the event
    '''
    if 'queryStringParameters' in event.keys():
        if event['queryStringParameters'] is not None:
            return event['queryStringParameters']
    return {}


def path_parameters(event):
    '''
      Function to handle getting path parameters out of the event
    '''
    if 'pathParameters' in event.keys():
        if event['pathParameters'] is not None:
            return event['pathParameters']
    return {}


def get_query_parameter_value(event, key_name):
    '''
      Function to fetch the value of a specific query parameter
    '''
    params = query_parameters(event)

    if key_name in params:
        return params[key_name]

    return None


def get_path_parameter_value(event, key_name):
    '''
      Function to fetch the value of a specific path parameter
    '''
    params = path_parameters(event)

    if key_name in params:
        return params[key_name]

    return None
