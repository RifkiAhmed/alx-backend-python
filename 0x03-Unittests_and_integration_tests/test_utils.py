#!/usr/bin/env python3
'''Test nested map module'''

from parameterized import parameterized
from typing import Any, Mapping, Sequence
import unittest

access_nested_map = __import__('utils').access_nested_map


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
