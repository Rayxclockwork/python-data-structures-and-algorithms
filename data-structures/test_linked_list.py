import pytest
from linked_list import LinkedList


def test_includes(new_list):
    assert new_list.includes(12)
    assert not new_list.includes(45)


def test_string(new_list):
    assert new_list.__str__


def test_insert():
    test_list = LinkedList()
    test_list.insert(1)
    assert test_list.head.value == 1


def test_append(new_list):
    assert new_list.append(8)


def test_insert_before(new_list):
    assert new_list.insert_before(5, 12)


def test_insert_after():
    assert LinkedList.insert_after(3, 8)


@pytest.fixture()
def new_list():
    print('in new list')
    test_list = LinkedList()
    for i in range(1, 20):
        test_list.insert(i)
    return test_list
