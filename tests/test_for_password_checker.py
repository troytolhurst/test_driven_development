import pytest 
from lib.password_checker import *

def test_password_if_longer_than_8():
    password = PasswordChecker()
    result = password.check("troy12345")
    assert result  == True

def test_is_shorter_than_8():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("troy")
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."
        


