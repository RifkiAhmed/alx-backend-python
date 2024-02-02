#!/usr/bin/env python3
'''Test module for nested map'''

from parameterized import parameterized
from typing import Any, Mapping, Sequence
import unittest
from unittest.mock import Mock, patch
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


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
        '''Test that get_json method returns what it is supposed to'''
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests.return_value = mock_response
        get_json_result = get_json(test_url)
        mock_requests.assert_called_once_with(test_url)
        self.assertEqual(get_json_result, test_payload)


class TestMemoize(unittest.TestCase):
    '''Class to test memoize decorator'''

    def test_memoize(self):
        '''Test memoize decorator'''
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_a_method:
            instance = TestClass()
            r1 = instance.a_property
            r2 = instance.a_property

            mock_a_method.assert_called_once()
            self.assertEqual(r1, 42)
            self.assertEqual(r2, 42)
