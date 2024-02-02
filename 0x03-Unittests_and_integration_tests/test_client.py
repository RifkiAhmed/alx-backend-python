#!/usr/bin/env python3
'''Test module for org method'''
from parameterized import parameterized
from unittest.mock import Mock, patch
import unittest

GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''class to test org method'''

    @parameterized.expand([
        ('google', {"login": True}),
        ('abc', {"login": False})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected_output, mock_get_json):
        '''Test that org method returns what it is supposed to'''
        mock_get_json.return_value = expected_output
        client = GithubOrgClient(org)
        org_info = client.org
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/" + org)
        self.assertEqual(org_info, expected_output)
