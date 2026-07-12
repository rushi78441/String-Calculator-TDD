import pytest
from string_calculator.calculator import add

def test_add_empty_string_return_zero():
    assert add("") == 0 , "String should be empty"
