#!/usr/bin/env python3
""" Testing the SUITE Unittest that module the Task """

from unittest import TestCase, mock

from parameterized import parameterized

from unittest.mock import patch, Mock

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

class TestGetJson(TestCase):
    """ Class for testing get_json function """
    # order of args: test_url, test_payload
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test method returns correct output """
        # set mock response to have return value of test payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        # function calls requests.get, need patch to get mock return value
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            # check that mocked method called once per input
            mock_response.json.assert_called_once()

class TestMemoize(TestCase):
    """ The class thats for the testing of the memoization """

    def test_memoize(self):
        """ Testing for the memoize's function """

        class TestClass:
            """ A Test's class """

            def a_method(self):
                """ The method thats to always just return 42 """
                return 42

            @memoize
            def a_property(self):
                """ Returning the memoized actual property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            testing_class = TestClass()
            realist_return = testing_class.a_property
            realist_return = testing_class.a_property

            self.assertEqual(realist_return, 42)
            patched.assert_called_once()
