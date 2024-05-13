#!/usr/bin/env python3
""" Testing for the utils for client """


import requests

import unittest

from unittest.mock import patch, Mock, PropertyMock, call

from parameterized import parameterized, parameterized_class

import utils

from utils import access_nested_map, get_json, memoize

from client import GithubOrgClient

import client

from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Testing so that the json can actually be gotten """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """ Testing for the org thats of the client """
        get_patch.return_value = expected
        c = GithubOrgClient(org)
        self.assertEqual(c.org, expected)
        get_patch.assert_called_once_with("https://api.github.com/orgs/"+org)

    def test_public_repos_url(self):
        """ testing so that the _public_repos_url actually
        works """
        expected = "www.yes.com"
        payload = {"repos_url": expected}
        too_mock = 'client.GithubOrgClient.org'
        with patch(too_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("c")
            self.assertEqual(cli._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """ test the public repos """
        name_jeff = {"name": "Jeff", "license": {"key": "a"}}
        name_bobb = {"name": "Bobb", "license": {"key": "b"}}
        name_suee = {"name": "Suee"}
        too_mock = 'client.GithubOrgClient._public_repos_url'
        get_json_mock.return_value = [name_jeff, name_bobb, name_suee]
        with patch(too_mock, PropertyMock(return_value="www.yes.com")) as y:
            g = GithubOrgClient("c")
            self.assertEqual(g.public_repos(), ['Jeff', 'Bobb', 'Suee'])
            self.assertEqual(g.public_repos("a"), ['Jeff'])
            self.assertEqual(g.public_repos("c"), [])
            self.assertEqual(g.public_repos(45), [])
            get_json_mock.assert_called_once_with("www.yes.com")
            y.assert_called_once_with()
