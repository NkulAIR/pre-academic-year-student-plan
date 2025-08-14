import pytest
from plates import is_valid

def main():
    test_plates()


def test_numplace():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_space():
    assert is_valid("AA") == True
    assert is_valid("A A") == False

def test_length():
    assert is_valid("AAAAAA") == False
    assert is_valid("AAAAAAA") == False

def test_zeroplace():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_alphanum():
    assert is_valid("AA22") == True
    # assert is_valid("AA 22") == False
    assert is_valid("AA@22") == False
