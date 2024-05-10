#!/usr/bin/env python3
""" Testing the SUITE Unittest that module the Task """

from unittest import TestCase, mock

from parameterized import parameterized

from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """ Classng for the testing of the Nested Map's function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """ Testing the methods that returns output """
        realist_output = access_nested_map(map, path)
        self.assertEqual(realist_output, expected_output)
