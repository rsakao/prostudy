import unittest
from src.recursive.recursive_03 import reverse_string

class ReverseStringTestCase(unittest.TestCase):
    def test_reverse_string_empty(self):
        self.assertEqual(reverse_string(''), '')

    def test_reverse_string_single_character(self):
        self.assertEqual(reverse_string('a'), 'a')
        self.assertEqual(reverse_string('z'), 'z')

    def test_reverse_string_multiple_characters(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string('world'), 'dlrow')
        self.assertEqual(reverse_string('python'), 'nohtyp')

if __name__ == '__main__':
    unittest.main()