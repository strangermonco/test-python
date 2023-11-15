# File: tests/test_add_five.py
from lib.check_codeword import *



def test_codeword_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_codeword_close():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_codeword_wrong():
    result = check_codeword("homey")
    assert result == "WRONG!"