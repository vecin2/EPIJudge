from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    left, right = 0, len(A) - 1

    while left < right:
        middle = (left + right) // 2

        if A[middle] > A[right]:
            left = middle + 1
        else:
            right = middle

    return right


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_shifted_sorted_array.py",
            "search_shifted_sorted_array.tsv",
            search_smallest,
        )
    )
