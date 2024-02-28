import unittest
from src.recursive.recursive_04 import binary_search, binary_search_copilot

class BinarySearchTestCase(unittest.TestCase):
    def test_binary_search_existing(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_binary_search_non_existing(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0), -1)
        self.assertEqual(binary_search([], 1), -1)

    def test_binary_search_copilot_existing(self):
        self.assertEqual(binary_search_copilot([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search_copilot([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(binary_search_copilot([1, 2, 3, 4, 5], 5), 4)

    def test_binary_search_copilot_non_existing(self):
        self.assertEqual(binary_search_copilot([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(binary_search_copilot([1, 2, 3, 4, 5], 0), -1)
        self.assertEqual(binary_search_copilot([], 1), -1)

if __name__ == '__main__':
    unittest.main()