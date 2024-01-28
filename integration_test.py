# Function 1
def multiply(x, y):
    return x * y

# Function 2 that depends on Function 1
def calculate_total(x, y):
    product = multiply(x, y)
    return product + 10

# Integration test for the interaction between the two functions
def test_integration():
    result = calculate_total(2, 3)
    assert result == 16  # Assert that the result is calculated correctly