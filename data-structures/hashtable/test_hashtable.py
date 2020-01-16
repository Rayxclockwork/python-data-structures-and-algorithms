from hashtable import Node, Hashtable
import pytest

def test_node_instance():
    node = Node('Cat', 'Sinead')
    assert node

def test_hashtable_instance():
    hashtable = Hashtable()
    assert hashtable


