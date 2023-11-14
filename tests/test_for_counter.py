from lib.counter import * 
def test_for_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_for_ten():
    counter = Counter()
    counter.add(10)
    assert counter.report() == 'Counted to 10 so far.'

def test_for_multiple():
    counter = Counter()
    counter.add(1)
    counter.add(2)
    counter.add(5)
    counter.add(10)
    counter.add(13)
    counter.add(28)
    assert counter.report() == 'Counted to 59 so far.'
