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

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license, expected):
        """ testing for the license's checker """
        self.assertEqual(GithubOrgClient.has_license(repo,
            license), expected)

class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ The integration's testing for the github's orgg client """

    @classmethod
    def setUpClass(cls):
        """ prepare for testing """
        orgg = TEST_PAYLOAD[0][0]
        reposi = TEST_PAYLOAD[0][1]
        orgg_mock = Mock()
        orgg_mock.json = Mock(return_value=orgg)
        cls.orgg_mock = orgg_mock
        reposi_mock = Mock()
        reposi_mock.json = Mock(return_value=reposi)
        cls.reposi_mock = reposi_mock

        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

        options = {cls.org_payload["repos_url"]: reposi_mock}
        cls.get.side_effect = lambda p: options.get(p, orgg_mock)

    @classmethod
    def tearDownClass(cls):
        """ The unprepared that's for testing """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ public reposi test """
        p = GithubOrgClient("c")
        self.assertEqual(p.orgg, self.org_payload)
        self.assertEqual(p.repos_payload, self.repos_payload)
        self.assertEqual(p.public_repos(), self.expected_repos)
        self.assertEqual(p.public_repos("NONEXISTENT"), [])
        self.get.assert_has_calls([call("https://api.github.com/orgs/c"),
                                   call(self.org_payload["repos_url"])])

    def test_public_repos_with_license(self):
        """ public reposi test """
        p = GithubOrgClient("c")
        self.assertEqual(p.orgg, self.org_payload)
        self.assertEqual(p.repos_payload, self.repos_payload)
        self.assertEqual(p.public_repos(), self.expected_repos)
        self.assertEqual(p.public_repos("NONEXISTENT"), [])
        self.assertEqual(p.public_repos("apache-2.0"), self.apache2_repos)
        self.get.assert_has_calls([call("https://api.github.com/orgs/c"),
                                   call(self.org_payload["repos_url"])])

