from tree_intersection import Hashtable, _Node, Queue, BinaryTree, tree_intersection, recurse_traverse
import pytest

def test_tree_instance():
    tree = BinaryTree()
    assert tree._root is None

def test_hashtable_instance():
    hashtable = Hashtable()
    assert hashtable

def test_add():
    test_table = Hashtable()
    test_table.add(5, 5)
    assert test_table.get(5) == 5

def test_empty_tree():
	tree_1 = BinaryTree()
	tree_2 = BinaryTree()
	tree_2.add(12)
	tree_2.add(14)
	tree_2.add(5)
	expected = []
	actual = tree_intersection(tree_1, tree_2)
	assert actual == expected

def test_tree_intersection():
	tree_1 = BinaryTree()
	tree_1.add(15)
	tree_1.add(12)
	tree_1.add(8)
	tree_1.add(5)
	tree_2 = BinaryTree()
	tree_2.add(12)
	tree_2.add(14)
	tree_2.add(5)
	tree_2.add(2)
	expected = [12, 5]
	actual = tree_intersection(tree_1, tree_2)
	assert actual == expected