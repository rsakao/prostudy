import unittest
from src.recursive.recursive_01 import fibonacci, fibonacci_copilot
import timeit

class FibonacciTestCase(unittest.TestCase):
    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_positive(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)

    def test_fibonacci_spped(self):
      execution_time = timeit.timeit('fibonacci(15)', globals=globals(), number=1000)
      print(f"fibonacci_speed Execution time: {execution_time} seconds")

class FibonacciOopilotTestCase(unittest.TestCase):
    def test_fibonacci_copilot_zero(self):
        self.assertEqual(fibonacci_copilot(0), 0)

    def test_fibonacci_copilot_positive(self):
        self.assertEqual(fibonacci_copilot(1), 1)
        self.assertEqual(fibonacci_copilot(2), 1)
        self.assertEqual(fibonacci_copilot(3), 2)
        self.assertEqual(fibonacci_copilot(4), 3)
        self.assertEqual(fibonacci_copilot(5), 5)
        self.assertEqual(fibonacci_copilot(6), 8)

    def test_fibonacci_copilot_speed(self):
      execution_time = timeit.timeit('fibonacci_copilot(15)', globals=globals(), number=1000)
      print(f"fibonacci_copilot_speed Execution time: {execution_time} seconds")

if __name__ == '__main__':
    unittest.main()