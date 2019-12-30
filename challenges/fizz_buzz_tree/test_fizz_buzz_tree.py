from fizz_buzz_tree import _Node, BinaryTree, fizz_buzz_tree
import pytest


def test_fizz_buzz():
	tree = BinaryTree()
	tree._root = _Node(3)
	tree._root.left = _Node(9)
	tree._root.right = _Node(15)
	tree._root.right.left = _Node(7)
	assert fizz_buzz_tree(tree)._root.value == 'Fizz'

def test_single_3():
	pass

def test_single_5():
	pass

def test_15():
	pass