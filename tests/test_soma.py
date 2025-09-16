 ```
# =======================================
#     Tests for sum function
# =======================================

import pytest

def test_soma_zero_zero():
    with pytest.raises(ValueError):
        soma(0, 0)

def test_soma_zero_nonzero():
    assert soma(0, 1) == 1

def test_soma_nonzero_zero():
    assert soma(1, 0) == 1

def test_soma_nonzero_nonzero():
    assert soma(2, 3) == 5
```