import unittest

# The function we want to test
def add(x, y):
    return x + y

# Create a test case class that inherits from unittest.TestCase
class TestAddition(unittest.TestCase):
    
    def test_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)  # Assert that the result is equal to 5

    def test_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)  # Assert that the result is equal to -5

    def test_mixed_numbers(self):
        result = add(2, -3)
        self.assertEqual(result, -1)  # Assert that the result is equal to -1

if __name__ == '__main__':
    unittest.main()
