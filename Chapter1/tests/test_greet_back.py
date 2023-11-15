# File: tests/test_add_five.py
from lib.greet import *

def test_greet_back():
    result = greet("shaun")
    assert result == "Hello, shaun!"