from array_binary_search import binary_search


def test_binary_search():
    expected = 2
    actual = binary_search([42, 15, 8, 16, 4], 15)
    assert expected == actual


def test_for_no_target():
    expected = -1
    actual = binary_search([4, 8, 15, 16, 23, 42], 3)
    assert expected == actual
