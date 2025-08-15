import pytest
from plates import is_valid

def test_order():
    assert is_valid("AA") == True
    assert is_valid("0A") == False

def test_alphabetical():
    assert is_valid("20") == False
    assert is_valid("0A") == False
    assert is_valid("2") == False

def test_numplace():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_length():
    assert is_valid("AAAAAAA") == False
    assert is_valid("AAA") == True
    assert is_valid("A") == False

def test_zeroplace():
    assert is_valid("AA200") == True
    assert is_valid("AAA022") == False
    assert is_valid("0AA") == False

def test_alphanum():
    assert is_valid("AA22") == True
    assert is_valid("AA 22") == False
    assert is_valid("AA@22") == False