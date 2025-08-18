import pytest
from fuel import convert, gauge

def main():
    test_fuel()


def test_convert():
    assert convert("1/2") == 50
    assert convert("10/70") == 14


def test_x():
    with pytest.raises(ValueError):
        convert("100/1")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_percentage():
    assert gauge(20) == f"{'20'}%"
    assert gauge(30) == f"{'30'}%"

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")


def test_empty():
    gauge(0) == "E"
    gauge(100) == "F"



if __name__ == "__main__":
    main()
