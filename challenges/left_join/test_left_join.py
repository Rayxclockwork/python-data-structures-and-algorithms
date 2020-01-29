
from left_join import Hashtable, left_join
import pytest

def test_hashtable_instance():
    hashtable = Hashtable()
    assert hashtable

def test_add():
    test_table = Hashtable()
    test_table.add('Home', 'Kansas City')
    assert test_table.get('Home') == 'Kansas City'


def test_left_join_null():
	ht_1 = Hashtable()
	ht_2 = Hashtable()
	ht_1.add('Happy', 'Joy')
	ht_2.add('guide', 'follow')
	assert left_join(ht_1, ht_2) == [['Happy', 'Joy', None]]