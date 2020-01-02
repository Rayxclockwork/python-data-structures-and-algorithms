from tree import BinaryTree, BinarySearchTree, Queue
import pytest


def test_tree_instance():
    tree = BinaryTree()
    assert tree._root is None


def test_tree_one_member():
    tree = BinarySearchTree()
    tree.add('apples')
    assert tree._root.value == 'apples'


def test_three_members():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    assert tree._root.value == 10
    assert tree._root.left.value == 5
    assert tree._root.right.value == 15

def test_in_order_empty():
    tree = BinarySearchTree()
    expected = []
    actual = tree.in_order()
    assert actual == expected

def test_pre_order_empty():
    tree = BinarySearchTree()
    expected = []
    actual = tree.pre_order()
    assert actual == expected

def test_post_order_empty():
    tree = BinarySearchTree()
    expected = []
    actual = tree.post_order()
    assert actual == expected


def test_pre_order():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    expected = [10, 5, 15]
    actual = tree.pre_order()
    assert expected == actual


def test_in_order():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    expected = [5, 10, 15]
    actual = tree.in_order()
    assert expected == actual


# def test_breadth_first():
#     tree = BinaryTree()
#     tree.add(10)
#     tree.add(5)
#     tree.add(15)
#     tree.add(7)
#     tree.add(3)
#     tree.add(12)
#     tree.add(6)
#     tree.add(18)

#     expected = [10, 5, 15, 3, 7, 12, 18, 6]
#     actual = BinaryTree.breadth_first(tree)
#     assert expected == actual

def test_find_max():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(7)
    tree.add(3)
    tree.add(12)
    tree.add(6)
    tree.add(18)

    expected = [10, 5, 15, 3, 7, 12, 18, 6]
    actual = BinaryTree.find_maximum_value(tree)
    assert expected == actual


def test_post_order():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    expected = [5, 15, 10]
    actual = tree.post_order()
    assert expected == actual


def test_contains_root_true():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    expected = True
    actual = tree.contains(10)
    assert expected == actual


def test_contains_node_true():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    expected = True
    actual = tree.contains(5)
    assert expected == actual


def test_contains_false():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    expected = False
    actual = tree.contains(12)
    assert expected == actual
