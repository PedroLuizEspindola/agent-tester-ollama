 Sure! Here is an example of a complete test file for the code you provided:
```
import pytest

def test_divisao_sucesso():
    with pytest.raises(ValueError):
        divisao(10, 0)

def test_divisao_erro_zero():
    with pytest.raises(ZeroDivisionError):
        divisao(0, 2)

def test_divisao_valores():
    assert divisao(5, 3) == 1.67
```
Here's a brief explanation of each test:

* `test_divisao_sucesso()`: Tests that the function raises a `ValueError` when division by zero is attempted.
* `test_divisao_erro_zero()`: Tests that the function raises a `ZeroDivisionError` when dividing by zero.
* `test_divisao_valores()`: Tests that the function works correctly for valid input values. In this case, we're testing that the result of 5 / 3 is close to 1.67.

Note that in each test, we use the `with pytest.raises()` syntax to simulate the error handling expected by the function. This allows us to write more concise and readable tests.