'''
Test parameters lib functions
'''

import unittest

from src.lib import path_parameters, get_path_parameter_value
from src.lib import query_parameters, get_query_parameter_value


EVENT = {
    'queryStringParameters': {
        'foo': 'bar'
    },
    'pathParameters': {
        'baz': 'quiz'
    }
}


class TestPathParameters(unittest.TestCase):
    '''
    Test path parameters handling
    '''
    def test_path_parameters(self):
        '''
        Test to verify return of path paras dict
        '''
        params = path_parameters(EVENT)
        self.assertEqual(params, EVENT['pathParameters'])

    def test_no_path_parameters(self):
        '''
        Test to verify handling missing path parameters as empty dict
        '''
        params = path_parameters({})
        self.assertEqual(params, {})

    def test_get_path_parameter_value(self):
        '''
        Test to verify get a specific named key's value
        '''
        param = get_path_parameter_value(EVENT, 'baz')
        self.assertEqual(param, EVENT['pathParameters']['baz'])

    def test_get_path_parameter_value_missing(self):
        '''
        Test to verify a missing key is returned as NoneType
        '''
        param = get_path_parameter_value(EVENT, 'bar')
        self.assertEqual(param, None)


class TestQueryParameters(unittest.TestCase):
    '''
    Test query parameters handling
    '''
    def test_query_parameters(self):
        '''
        Test to verify return of query params dict
        '''
        params = query_parameters(EVENT)
        self.assertEqual(params, EVENT['queryStringParameters'])

    def test_no_query_parameters(self):
        '''
        Test to verify handling missing query parameters as empty dict
        '''
        params = query_parameters({})
        self.assertEqual(params, {})

    def test_get_query_parameter_value(self):
        '''
        Test to verify get a specific named key's value
        '''
        param = get_query_parameter_value(EVENT, 'foo')
        self.assertEqual(param, EVENT['queryStringParameters']['foo'])

    def test_get_query_parameter_value_missing(self):
        '''
        Test to verify a missing key is returned as NoneType
        '''
        param = get_query_parameter_value(EVENT, 'bar')
        self.assertEqual(param, None)
