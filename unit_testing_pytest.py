# Function to be tested
def add(x, y):
    return x + y

# Test function for unit testing with pytest
def test_positive_numbers():
    result = add(2, 3)
    assert result == 5  # Assert that the result is equal to 5

def test_negative_numbers():
    result = add(-2, -3)
    assert result == -5  # Assert that the result is equal to -5