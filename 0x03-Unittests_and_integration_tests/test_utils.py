#!/usr/bin/env python3
'''Test module for nested map'''

from parameterized import parameterized
from typing import Any, Mapping, Sequence
import unittest
from unittest.mock import Mock, patch
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json

class TestAccessNestedMap(unittest.TestCase):
    '''Class to test access_nested_map method'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        '''Test that access_nested_map method returns what it is supposed to'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        '''Test KeyError cases for access_nested_map method'''
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Class to test get_json method'''
    
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests):
        ''''''
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests.return_value = mock_response
        get_json_result = get_json(test_url)
        mock_requests.assert_called_once_with(test_url)
        self.assertEqual(get_json_result, test_payload)
