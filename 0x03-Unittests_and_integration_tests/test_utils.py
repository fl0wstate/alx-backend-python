#!/usr/bin/env python3

"""Simple test case for nested map"""
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test Case for access nested map"""
    @parameterized.expand([
       ({"a": 1}, ("a",), 1),
       ({"a": {"b": 2}}, ("a",), {"b": 2}),
       ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test case for the access nested map func"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map, path, err):
        """Handling all the key errors passed"""
        with self.assertRaises(err):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Testing the get_json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json returns the expected result"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call get_json with test_url and assert the result
        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        # Assert that requests.get was called once with the test_url
        mock_get.assert_called_once_with(test_url)
