from lib.string_builder import * 

def test_for_string_builder_hello():
    string = StringBuilder()
    string.add('hello')
    assert string.output() == "hello"

def test_for_string_builder_size_hello():
    string = StringBuilder()
    string.add("hello")
    string.size()
    assert string.size() == 5

def test_for_string_builder_long_string():
    string = StringBuilder()
    string.add('thisisareallyreallyreallylongstring')
    string.add('thisisnt')
    assert string.size() == 43