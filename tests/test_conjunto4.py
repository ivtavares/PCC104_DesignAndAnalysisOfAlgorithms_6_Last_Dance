import pytest

from conjuntos.conjunto4 import SubsetSum

input_sum_output = [
    ({1, 2, 5, 6, 8}, 9, [{1, 2, 6}, {1, 8}]),
    ({3, 5, 6, 7}, 15, [{3, 5, 7}]),
    ({10, 20, 15, 5}, 25, [{10, 15}, {20, 5}]),
    ({2, 4, 6, 8}, 5, []),
]


@pytest.mark.parametrize("input_set,required_sum,output_list_set", input_sum_output)
def test_subset_sum(input_set, required_sum, output_list_set):
    result = SubsetSum().subset_sum(input_set, required_sum)
    for r in result:
        assert r in output_list_set
