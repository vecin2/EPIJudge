from typing import List

from test_framework import generic_test


def search_first_greater_than_k(A: List[int], k: int) -> int:
    return iterative_search(A, 0, len(A) - 1, k, -1)


def iterative_search(A, low, high, target, result):
    while high >= low:
        m = (high + low) // 2

        if A[m] == target:
            low = m + 1
        elif A[m] < target:
            low = m + 1
        else:  # A[m] > target
            result = m
            high = m - 1

    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "11.1_v1_search_first_key.py",
            "search_first_greater_than_key.tsv",
            search_first_greater_than_k,
        )
    )
