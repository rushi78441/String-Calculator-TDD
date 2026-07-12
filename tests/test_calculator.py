import pytest
from string_calculator.calculator import add

# Empty String test
def test_add_empty_string_return_zero():
    assert add("") == 0 , "String should be empty"

# Single number test
def test_add_single_number():
    assert add("5") == 5, "single number 5 should be added"
    assert add("10") == 10, "single number 10 should be added"
