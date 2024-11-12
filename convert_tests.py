import convert
import unittest


class TestCases(unittest.TestCase):

    def test_str_to_float1(self):
        string = 'not convertable'
        result = convert.str_to_float(string)
        expected = None
        self.assertEqual(result, expected)

    def test_str_to_float2(self):
        string = '34.5'
        result = convert.str_to_float(string)
        expected = 34.5
        self.assertEqual(result, expected)
