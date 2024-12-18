import pytest

from conjuntos.conjunto2 import knapsack, MemoryKnapsack


weight_value_capacity_and_optimal_solution = [
    ([2, 1, 3, 2], [12, 10, 20, 15], 5, 37),  # Solução ótima: itens 1, 2 e 4
    ([1, 2, 3], [10, 15, 40], 6, 65),  # Solução ótima: todos os itens
    ([4, 5, 6], [10, 20, 30], 3, 0),  # Solução ótima: nenhum item
    ([2, 3, 4, 5], [3, 4, 5, 6], 5, 7),  # Solução ótima: itens 1 e 2
]


@pytest.mark.parametrize(
    "weight,value,capacity,optimal_solution",
    weight_value_capacity_and_optimal_solution,
)
def test_knapsack(weight, value, capacity, optimal_solution):
    assert knapsack(weight, value, capacity) == optimal_solution


@pytest.mark.parametrize(
    "weight,value,capacity,optimal_solution",
    weight_value_capacity_and_optimal_solution,
)
def test_memory_knapsack(weight, value, capacity, optimal_solution):
    assert (
        MemoryKnapsack().memory_knapsack(weight, value, capacity) == optimal_solution
    )
