# File: tests/test_string_builder.py
import pytest
from lib.password_checker import *

def test_check_more_than_8():
    checker = PasswordChecker()
    assert checker.check("12345678910") == True

def test_check_less_than_8():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check("123")
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."

def test_empty_password():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check("")
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."

