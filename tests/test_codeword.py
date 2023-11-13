from lib.check_codeword import *

def test_codeword_for_hello():
    result = check_codeword('hello')
    assert result == "WRONG!"

def test_codeword_for_horse():
    result = check_codeword('horse')
    assert result == 'Correct! Come in.'

def test_codeword_for_howe():
    result = check_codeword('howe')
    assert result == "Close, but nope."