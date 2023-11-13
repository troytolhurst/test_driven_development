from lib.report_length import *

def test_report_length_17():
    result = report_length('17')
    assert result == "This string was 2 characters long."

def test_report_length_thisisreallyreallyreallylong():
    result = report_length('thisisreallyreallyreallylong')
    assert result == "This string was 28 characters long."