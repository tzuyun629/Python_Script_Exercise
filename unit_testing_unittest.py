import unittest

# Function to be tested
def add(x, y):
    return x + y

# Test class for unit testing with unittest
class TestAddition(unittest.TestCase):
    def setUp(self):
        self.args = (3, 6)

    def tearDown(self):
        self.args = None

    def test_positive_numbers(self):
        expected = 5
        result = add(*self.args)
        self.assertEqual(expected, result)  # Assert that the result is equal to 5

    def test_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)  # Assert that the result is equal to -5

if __name__ == '__main__':
    unittest.main()