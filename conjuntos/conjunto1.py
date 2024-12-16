from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) > 1:
        half = len(arr) // 2
        arr_b = arr[:half]
        arr_c = arr[half:]
        arr_b = merge_sort(arr_b)
        arr_c = merge_sort(arr_c)
        return merge(arr_b, arr_c, arr)
    return arr


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