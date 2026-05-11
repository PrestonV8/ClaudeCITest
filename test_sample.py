def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0


def test_add_floats():
    assert add(1.5, 2.5) == 4.0


def test_subtract():
    assert subtract(10, 4) == 6


def test_subtract_negative_result():
    assert subtract(3, 7) == -4


def test_multiply():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(5, 0) == 0


def test_multiply_negative():
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5.0


def test_divide_float_result():
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
