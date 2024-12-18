from typing import Set, List


class SubsetSum:
    def __init__(self) -> None:
        self.output_set = list()
        self.current_result = set()

    def subset_sum(self, input: Set[int], required_sum: int) -> List[Set[int]]:
        current_input = input.copy()
        while current_input:
            i = current_input.pop()
            current_sum = required_sum - i

            if current_sum == 0:
                result = self.current_result.copy()
                result.add(i)
                self.output_set.append(result)
            elif current_sum > 0:
                self.current_result.add(i)
                self.subset_sum(current_input, current_sum)
                self.current_result.remove(i)

        return self.output_set
