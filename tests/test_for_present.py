import pytest
from lib.present import *
def test_for_wrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

def test_wrap_when_wrapped_already():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    message = str(e.value)
    assert message == "A contents has already been wrapped."

def test_wrapping_already_wrapped_preserves_value():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    assert present.unwrap() == 44

    