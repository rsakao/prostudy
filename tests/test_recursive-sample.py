import unittest
from src.recursive.recursive_sample import factorial

class FactorialTestCase(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(15), 1307674368000)

if __name__ == '__main__':
    unittest.main()