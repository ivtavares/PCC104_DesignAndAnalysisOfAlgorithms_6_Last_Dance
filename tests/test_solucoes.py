import pytest

from conjuntos import solucoes as s


unsorted_and_sorted_lists = [
    ([3, 1, 2], [1, 2, 3]),
    ([10, 5, 7, 1], [1, 5, 7, 10]),
    ([9, 4, 8, 2, 6], [2, 4, 6, 8, 9]),
    ([9, 8, 6, 4, 2], [2, 4, 6, 8, 9]),
]


@pytest.mark.parametrize("unsorted_list,sorted_list", unsorted_and_sorted_lists)
def test_conjunto_1_merge_sort(unsorted_list, sorted_list):
    assert s.Conjunto1.merge_sort(unsorted_list) == sorted_list


weight_value_capacity_and_optimal_solution = [
    ([2, 1, 3, 2], [12, 10, 20, 15], 5, 37),  # Solução ótima: itens 1, 2 e 4
    ([1, 2, 3], [10, 15, 40], 6, 65),  # Solução ótima: todos os itens
    ([4, 5, 6], [10, 20, 30], 3, 0),  # Solução ótima: nenhum item
    ([2, 3, 4, 5], [3, 4, 5, 6], 5, 7),  # Solução ótima: itens 1 e 2
]


class TestConjunto2:
    @pytest.mark.parametrize(
        "weight,value,capacity,optimal_solution",
        weight_value_capacity_and_optimal_solution,
    )
    def test_conjunto_2_knapsack(self, weight, value, capacity, optimal_solution):
        assert s.Conjunto2.knapsack(weight, value, capacity) == optimal_solution
    
    @pytest.mark.parametrize(
        "weight,value,capacity,optimal_solution",
        weight_value_capacity_and_optimal_solution,
    )
    def test_conjunto_2_memory_knapsack(self, weight, value, capacity, optimal_solution):
        assert s.Conjunto2.memory_knapsack(weight, value, capacity) == optimal_solution
