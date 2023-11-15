# File: tests/test_diary.py
from lib.diary import *

def test_snippet():
    #snippet = make_snippet("123")
    #snippet = diary.make_snippet()
    #assert snippet == "This is less than 5"
    pass

def test_check_string_is_5():
    snippet = make_snippet("hello this is a test")
    assert snippet == ("hello this is a test")

def test_check_string_is_less_than_5():
    snippet = make_snippet("hello test")
    assert snippet == ("hello test")

def test_check_string_more_than_5():
    snippet = make_snippet("hello this is a second test...")
    assert snippet == "hello this is a second..."
 