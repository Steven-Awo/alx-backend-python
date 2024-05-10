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

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """ Testing the method that raises the corrected exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)
