from lib.greet import*

def test_greet_returns_hello_troy_for_troy():
    result = greet('Troy')
    assert result == "Hello, Troy!"

def test_greet_returns_hello_sam_for_sam():
    result = greet('sam')
    assert result == "Hello, sam!"

def test_greet_returns_hello_caleb_for_caleb():
    result = greet('Caleb')
    assert result == 'Hello, Caleb!'