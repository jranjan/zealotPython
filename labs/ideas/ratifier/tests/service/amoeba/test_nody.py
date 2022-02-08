import pytest
import math


@pytest.mark.miniqual
@pytest.mark.qual
@pytest.mark.fullqual
def test_square_root():
    x = 10
    r = x * x
    assert r == 100, "Square commuted incorrectly"


@pytest.mark.qual
@pytest.mark.fullqual
def test_cube_root():
    x = 10
    r = x * x * x
    print(r)
    assert r == 1000, "Cube commuted incorrectly"


@pytest.mark.fullqual
def test_sqrt():
    x = 16
    r = math.sqrt(x)
    assert r == 4, "Cube commuted incorrectly"
