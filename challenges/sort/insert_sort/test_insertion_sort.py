from insertion_sort import insertion_sort
import pytest


def test_insertion_sort():
	arr = [10, 3, 15, 8, 20]
	expected = [3, 8, 10, 15, 20]
	assert insertion_sort(arr) == expected