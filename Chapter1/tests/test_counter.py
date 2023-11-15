# File: tests/test_counter.py
from lib.counter import *

def test_init():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_add():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

