import pytest

from conjuntos.conjunto1 import merge_sort


unsorted_and_sorted_lists = [
    ([3, 1, 2], [1, 2, 3]),
    ([10, 5, 7, 1], [1, 5, 7, 10]),
    ([9, 4, 8, 2, 6], [2, 4, 6, 8, 9]),
    ([9, 8, 6, 4, 2], [2, 4, 6, 8, 9]),
]


@pytest.mark.parametrize("unsorted_list,sorted_list", unsorted_and_sorted_lists)
def test_merge_sort(unsorted_list, sorted_list):
    assert merge_sort(unsorted_list) == sorted_list
