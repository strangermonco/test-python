# File: tests/test_string_builder.py
from lib.string_builder import *

def test_init():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

def test_add():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.output() == "hello"


def test_size():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.size() == 5

def test_add_multiple_strings():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add("world")
    string_builder.add("friend")
    assert string_builder.output() == "helloworldfriend"

def test_size_multiple():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add("world")
    string_builder.add("friend")
    assert string_builder.size() == 16