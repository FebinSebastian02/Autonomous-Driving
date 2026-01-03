import pytest  # python testing library is imported


# pytest: to automatically verify correct behavior(no need of manually checking like 10/2, 10/3, 10/0 etc. each time)
# ,including failure handling (code is wrong if it doesn't raise value error when divided by 0 - pytest checks how the
# code fails)
# , so changes don't break existing functionality(it detects if the code changes later).
# eg: if check is not given in divide(), zero division error is raised and test fails.

# Todo: Exceptions in pytest
# tests are usually written in separate file.
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")  # value error: bad value passed in
    return a / b

# test code. if a value error happens inside this block, the test passes. If no error, test fails.
def test_divide_by_zero():  # pytest only requires functions prefixed with test_ to discover them.
    with pytest.raises(ValueError, match="Division by zero"):  # check exception message contains this text exactly.
        divide(10, 0)
