from tree_intersection import _Node, Queue, BinaryTree, tree_intersection
import pytest


def test_binary_tree():
    tree_one = BinaryTree()
    tree_one.add(12)
    tree_one.add(5)
    tree_one.add(3)
    tree_one.add(15)
    tree_two = BinaryTree()
    tree_two.add(1)
    tree_two.add(5)
    tree_two.add(12)
    tree_two.add(55)
    assert tree_one._root.value == 12
    assert tree_two._root.value == 1
    assert tree_one._root.left.value == 5

def test_tree_instance():
    tree = BinaryTree()
    assert tree._root is None

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
	expected = [5, 12]
	actual = tree_intersection(tree_1, tree_2)
	assert actual == expected