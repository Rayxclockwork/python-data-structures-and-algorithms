from hashtable import Hashtable
import pytest

def test_hashtable_instance():
    hashtable = Hashtable()
    assert hashtable

def test_add():
    test_table = Hashtable()
    test_table.add('Home', 'Kansas City')
    assert test_table.get('Home') == 'Kansas City'

def test_get_in_list():
    new_hashtable = Hashtable()
    new_hashtable.add('Candy', 'Crunch')
    assert new_hashtable.get('Candy') == 'Crunch'


def test_contains():
    new_hashtable = Hashtable()
    new_hashtable.add('Soda', 'MtnDew')
    assert new_hashtable.contains('Soda') == True

def test_does_not_contain():
    new_hashtable = Hashtable()
    assert new_hashtable.contains('Couch') == False

@pytest.mark.skip
def test_get_empty():
    hashtable = Hashtable()
    assert hashtable.get(None) == KeyError

@pytest.mark.skip
def test_get_not_in_list(new_hashtable):
    assert new_hashtable.get('Couch') == KeyError

