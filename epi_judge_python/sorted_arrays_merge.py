import heapq
from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    iterators = [iter(sorted_array) for sorted_array in sorted_arrays]

    min_heap = []

    for index, iterator in enumerate(iterators):
        value = next(iterator, None)

        if value is not None:
            heapq.heappush(min_heap, (value, index))

    result = []

    while min_heap:
        value, index = heapq.heappop(min_heap)
        result.append(value)
        new_value = next(iterators[index], None)

        if new_value is not None:
            heapq.heappush(min_heap, (new_value, index))

    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_arrays_merge.py", "sorted_arrays_merge.tsv", merge_sorted_arrays
        )
    )
