from quick_sort import partition, swap, quick_sort
import pytest

def test_partition():
	arr = [0, 5, 2, 6, 8, 4]

	pivot_index = partition(arr, 0, len(arr) - 1)

	assert arr == [0, 2, 4, 6, 8, 5]

	assert pivot_index == 2


def test_quick_sort():
	arr = [0, 5, 2, 6, 8, 4]
	quick_sort(arr, 0, len(arr) -1)
	assert arr == [0, 2, 4, 5, 6, 8]