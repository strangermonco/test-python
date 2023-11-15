# File: tests/test_counter.py
from lib.gratitudes import *

def test_init():
    gratitude = Gratitudes()
    assert gratitude.format()

def test_add():
    gratitude = Gratitudes()
    gratitude.add("food")
    assert gratitude.gratitudes == ["food"]

def test_format():
    gratitude = Gratitudes()
    formatted = gratitude.format()
    assert formatted == "Be grateful for: "

def single_gratitude():
    gratitude = Gratitudes()
    gratitude.add("Love")
    formatted = gratitudes.format()
    assert formatted == "Be grateful for: Love"

def multi_gratitude():
    gratitude = Gratitudes()
    gratitude.add("Cheese")
    gratitude.add("Sun")
    formatted = gratitudes.format()
    assert formatted == "Be grateful for: Cheese, Sun"

#def test_format():
#    gratitude = Gratitudes()
#    assert gratitude.format 