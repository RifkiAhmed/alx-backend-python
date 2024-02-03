#!/usr/bin/env python3
"""Test module for org method"""
from parameterized import parameterized
from unittest.mock import MagicMock, patch, PropertyMock
import unittest

GithubOrgClient = __import__("client").GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """class to test org method"""

    @parameterized.expand([
        ("google", {"login": True}),
        ("abc", {"login": False})
    ])
    @patch("client.get_json")
    def test_org(self, org, expected_output, mock_get_json) -> None:
        """Test that org method returns what it is supposed to"""
        mock_get_json.return_value = expected_output
        client = GithubOrgClient(org)
        org_info = client.org
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/" + org)
        self.assertEqual(org_info, expected_output)

    def test_public_repos_url(self) -> None:
        """Test that _public_repos_url returns what it is supposed to"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            url = "https://api.github.com/orgs/abc"
            mock_org.return_value = {"repos_url": url}
            client = GithubOrgClient("abc")
            repos_url = client._public_repos_url
            self.assertEqual(repos_url, url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Test that public_repos returns what it is supposed to"""
        repos = [
            {
                "name": "alx-interview",
                "license": {"key": "your_license"}
            },
            {
                "name": "alx-backend_python",
                "license": {"key": "my_license"}
            },
            {
                "name": "alx-backend_storage"
            },
            {
                "name": "alx-backend_javascript",
                "license": {"key": "your_license"}
            }

        ]
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            url = "https://api.github.com/orgs/abc"
            mock_public_repos_url.return_value = url
            mock_get_json.return_value = repos
            client = GithubOrgClient("abc")
            public_repos = client.public_repos("my_license")

            self.assertEqual(public_repos, ["alx-backend_python"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_value):
        """Test that has_license method returns what it is supposed to"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected_value)
