import pytest


@pytest.mark.miniqual
@pytest.mark.qual
@pytest.mark.fullqual
def test_add():
    x = 10
    y = 10
    r = x + y
    assert r == 20


@pytest.mark.miniqual
@pytest.mark.qual
@pytest.mark.fullqual
def test_subtract():
    x = 10
    y = 10
    r = x - y
    assert r == 0


@pytest.mark.miniqual
@pytest.mark.qual
@pytest.mark.fullqual
def test_multiply():
    x = 10
    y = 10
    r = x * y
    assert r == 100


@pytest.mark.miniqual
@pytest.mark.qual
@pytest.mark.fullqual
def test_divide():
    x = 10
    y = 10
    r = x / y
    assert r == 1


@pytest.mark.miniqual
@pytest.mark.qual
@pytest.mark.fullqual
def test_residue():
    x = 10
    y = 10
    r = x % y
    assert r == 0
