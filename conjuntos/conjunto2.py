from typing import List


def knapsack(
    weights: List[int], values: List[int | float], capacity: int
) -> int | float:
    size = len(weights)
    matrix = [[0] * (capacity + 1) for _ in range(size + 1)]

    for i in range(1, size + 1):
        for j in range(1, capacity + 1):
            if j - weights[i - 1] >= 0:
                matrix[i][j] = max(
                    matrix[i - 1][j],
                    values[i - 1] + matrix[i - 1][j - weights[i - 1]],
                )
            else:
                matrix[i][j] = matrix[i - 1][j]
    return matrix[-1][-1]


class MemoryKnapsack:
    def memory_knapsack(
        self, weights: List[int], values: List[int | float], capacity: int
    ) -> int | float:
        size = len(weights)
        self.weights = weights
        self.values = values
        self.matrix = [
            [0 if i == 0 or j == 0 else -1 for i in range(capacity + 1)]
            for j in range(size + 1)
        ]

        return self.mf_knapsack(size, capacity)

    def mf_knapsack(self, i: int, j: int) -> int | float:
        if self.matrix[i][j] < 0:
            if j < self.weights[i - 1]:
                value = self.mf_knapsack(i - 1, j)
            else:
                value = max(
                    self.mf_knapsack(i - 1, j),
                    self.values[i - 1]
                    + self.mf_knapsack(i - 1, j - self.weights[i - 1]),
                )
            self.matrix[i][j] = value
        return self.matrix[i][j]
