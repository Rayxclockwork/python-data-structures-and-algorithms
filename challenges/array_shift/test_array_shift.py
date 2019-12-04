from array_shift import insert_shift_array


def test_middle_shift():
  expected = [1, 2, 3, 4, 5]
  actual = [1, 2, 4, 5], 3
  assert expected is actual, "3 should be at middle index"
  