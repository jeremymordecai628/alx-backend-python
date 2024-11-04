#!/usr/bin/python3
"""
Unit tests for the `utils.access_nested_map` function.

This module includes tests for both normal cases, where the function should
return a valid result, and error cases, where it should raise a KeyError.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for the `access_nested_map` function in the utils module.

    This class contains test methods to verify that the `access_nested_map`
    function behaves as expected with both valid inputs and error cases.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test `access_nested_map` with valid inputs to verify it returns
        the expected results.

        Args:
            nested_map (dict): The dictionary with nested structures to access.
            path (tuple): The sequence of keys to retrieve the value from.
            expected (any): The expected result from accessing the nested map.

        Asserts:
            The function returns the expected result for each input set.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test `access_nested_map` to verify it raises a KeyError for invalid keys.

        Args:
            nested_map (dict): The dictionary with nested structures to access.
            path (tuple): The sequence of keys that will lead to a KeyError.

        Asserts:
            A KeyError is raised with the message containing the last missing key.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")
