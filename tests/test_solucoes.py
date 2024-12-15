import pytest

from conjuntos import solucoes as s


unsorted_and_sorted_lists = [
    ([3, 1, 2], [1, 2, 3]),
    ([10, 5, 7, 1], [1, 5, 7, 10]),
    ([9, 4, 8, 2, 6], [2, 4, 6, 8, 9]),
]


@pytest.mark.parametrize("array,sorted_array", unsorted_and_sorted_lists)
def test_conjunto_1_merge_sort(array, sorted_array):
    assert s.merge_sort(array) == sorted_array
