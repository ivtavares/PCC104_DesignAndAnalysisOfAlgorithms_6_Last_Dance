from typing import List


class Conjunto1:
    @staticmethod
    def merge_sort(arr: List[int]) -> List[int]:
        if len(arr) > 1:
            half = len(arr) // 2
            arr_b = arr[:half]
            arr_c = arr[half:]
            arr_b = Conjunto1.merge_sort(arr_b)
            arr_c = Conjunto1.merge_sort(arr_c)
            return Conjunto1.merge(arr_b, arr_c, arr)
        return arr

    @staticmethod
    def merge(arr_b: List[int], arr_c: List[int], arr_a: List[int]) -> List[int]:
        i = j = k = 0
        p = len(arr_b)
        q = len(arr_c)

        while i < p and j < q:
            if arr_b[i] <= arr_c[j]:
                arr_a[k] = arr_b[i]
                i += 1
            else:
                arr_a[k] = arr_c[j]
                j += 1
            k += 1
        if i == p:
            return arr_a[:k] + arr_c[j:]
        return arr_a[:k] + arr_b[i:]


class Conjunto2:
    @staticmethod
    def knapsack(
        weight: List[int], value: List[int | float], capacity: int
    ) -> int | float:
        size = len(weight)
        matrix = [[0] * (capacity + 1) for _ in range(size + 1)]

        for i in range(1, size + 1):
            for j in range(1, capacity + 1):
                if j - weight[i - 1] >= 0:
                    matrix[i][j] = max(
                        matrix[i - 1][j],
                        value[i - 1] + matrix[i - 1][j - weight[i - 1]],
                    )
                else:
                    matrix[i][j] = matrix[i - 1][j]
        return matrix[-1][-1]

    @staticmethod
    def memory_knapsack(
        weight: List[int], value: List[int | float], capacity: int
    ) -> int | float:
        return 0
