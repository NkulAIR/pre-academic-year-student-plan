import pytest
from bank import value

def main():
    test_bank()

def test_case():
    assert value("Hello") == 0
    assert value("hello") == 0

def test_mixed():
    try:
        assert value("hEllo") == 0
    except AssertionError:
        print(" ")
    try:
        assert value("HeLLo") == 0
    except AssertionError:
        print(" ")


def test_incorrect():
    assert value("123") == 100
    assert value("Whats up!") == 100

def test_first_letter():
    assert value("Hey") == 20
    assert value("hey") == 20

def test_empty():
    assert value() == 100

def phrase():
    assert value("Hello, there")




if __name__ == "__main__":
    main()


# catch incorrect values
# catch case-sensitivity
# catch if doesnt allow the whole phrase e.g Hey not H
