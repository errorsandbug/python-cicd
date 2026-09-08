from app import add


def test_addition():
    assert add(10, 20) == 30


def test_zero():
    assert add(0, 0) == 0


def test_negative():
    assert add(-10, 20) == 10