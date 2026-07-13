import pytest
from string_calculator.calculator import add

# Empty String test
def test_add_empty_string_return_zero():
    assert add("") == 0 , "String should be empty"

# Single number test
def test_add_single_number():
    assert add("5") == 5, "single number 5 should be added"
    assert add("10") == 10, "single number 10 should be added"

# Two Number test
def test_add_two_number():
    assert add("1,2") == 1 + 2 , "1 + 2 == 3"
    assert add("3,4") == 3 + 4, "3 + 4 == 7"

# Multiple numbers seperated with comma test
def test_add_multiple_numbers():
    assert add("1,2") == 1 + 2
    assert add("1,2,3,4,5") == 1 + 2 + 3 + 4 + 5  

# Support New line as delimeter test : “1\n2,3”
def test_support_new_line_as_delimeter():
    assert add("1\n2,3") == 6

# Support Custom Delimeter (//) test :  “//[delimiter]\n[numbers…]”
def test_support_custom_delimeter():
    assert add("//;\n1;2;3") == 6
    assert add("//*\n1*3*4") == 8


# Negative Number not allowed test
def test_negative_numbers_raise_valueError():
    with pytest.raises(ValueError) as exc_info:
        add("1,-2,-4")
    assert "negatives not allowed : -2, -4" in str(exc_info.value)

# Number > 1000 is npt allowed test
def test_num_gt_Thousand_raise_valueError():
    with pytest.raises(ValueError) as exc_info:
        add("1,10000,3,2000")
    assert "Numbers Greater than 1000 not allowed : 10000, 2000" in str(exc_info)