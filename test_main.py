import unittest
from main import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()
