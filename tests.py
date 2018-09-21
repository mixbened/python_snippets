# Test Functions
from calculations import numbers_sum, lowercase, main
from geogame import geogame


def test_numbers_sum():
    assert numbers_sum(1,2) == 3

def test_lowercase():
    assert lowercase('Haiii') == 'haiii'

test_numbers_sum()