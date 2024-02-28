import unittest
from src.recursive.recursive_02 import sum_list

class SumListTestCase(unittest.TestCase):
    def test_sum_list_empty(self):
        self.assertEqual(sum_list([]), 0)

    def test_sum_list_single_element(self):
        self.assertEqual(sum_list([5]), 5)
        self.assertEqual(sum_list([-10]), -10)

    def test_sum_list_multiple_elements(self):
        self.assertEqual(sum_list([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_list([-1, -2, -3, -4, -5]), -15)
        self.assertEqual(sum_list([10, -5, 3, 8]), 16)

if __name__ == '__main__':
    unittest.main()