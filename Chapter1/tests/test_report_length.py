# File: tests/test_report_length.py
from lib.report_length import *

def test_report_length():
    result = report_length("five")
    assert result == "This string was 4 characters long."