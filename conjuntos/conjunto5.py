from typing import List
from collections import deque


def branch_and_bound(
    weights: List[int], values: List[int | float], capacity: int
) -> int | float:
    items = [
        {"w": weight, "v": values[i], "v/w": values[i] / weight}
        for i, weight in enumerate(weights)
    ]
    items = deque(sorted(items, key=lambda payoff: payoff["v/w"], reverse=True))
    w = 0
    v = 0
    W = capacity
    while items:
        item = items.popleft()
        if w + item["w"] <= W:
            if items:
                v_w = items[0]["v/w"]
                in_ub = v + item["v"] + ((W - (item["w"] + w)) * v_w)
                out_ub = v + ((W - w) * v_w)

                if in_ub > out_ub:
                    v += item["v"]
                    w += item["w"]
            else:
                v += item["v"]
                w += item["w"]

    return v
