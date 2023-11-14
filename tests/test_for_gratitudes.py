from lib.gratitudes import *

def test_for_gratitude_dogs():
    gratitude = Gratitudes()
    gratitude.add("dogs")
    assert gratitude.format() == 'Be grateful for: dogs'

def test_for_gratitude_dogs_rainbows_xbox():
    gratitude = Gratitudes()
    gratitude.add('dogs')
    gratitude.add("rainbows")
    gratitude.add("xbox")
    assert gratitude.format() == 'Be grateful for: dogs, rainbows, xbox'
    