from linked_list import LinkedList, Node
import pytest


def test_includes():
    assert LinkedList.includes(LinkedList, 12) is True


def test_doesnt_include():
    assert LinkedList.includes(LinkedList, 34) is False


def test_string():
    assert LinkedList.__str__ == []


def test_init():
    assert LinkedList() == []


def test_insert():
    assert LinkedList.insert() == []
