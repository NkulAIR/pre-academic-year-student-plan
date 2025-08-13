import pytest
from twttr import shorten

def main():
    test_twttr()

def test_num():
    assert shorten("123") == "123"

def test_shorten():
    assert shorten("WORLD") == "WRLD"
    assert shorten("lowercase") == "lwrcs"
    assert shorten("RYTHM") == "RYTHM"
    assert shorten("rhythm") == "rhythm"

def test_punctuation():
    assert shorten("!&*") == "!&*"



if __name__ == "__main__":
    main()
