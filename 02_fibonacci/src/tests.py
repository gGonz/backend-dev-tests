import unittest

from timeit import default_timer as timer

from .fibonacci import fibonacci


class FibonacciTestCase(unittest.TestCase):

    def test_sequence(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        result = [fibonacci(i) for i in range(10)]
        self.assertEqual(result, expected)

    def test_error(self):
        with self.assertRaises(ValueError) as ctx:
            fibonacci(-1)
        self.assertEqual("Invalid number", str(ctx.exception))

    def test_memoization(self):
        start = timer()
        result = fibonacci(100)
        end = timer()
        self.assertEqual(result, 354224848179261915075)
        self.assertTrue((end - start) < 1)
