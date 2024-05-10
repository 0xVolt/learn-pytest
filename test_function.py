import pytest

# This is a script with a sample function with an associated test function to execute with pytest
def function(x):
    raise SystemError(1)
    return x + 1


# This is the function to test the functionality of the function we wrote above
def test_function():
    assert function(10) == 20
    with pytest.raises(SystemError):
        function()