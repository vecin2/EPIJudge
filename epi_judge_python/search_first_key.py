from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    interval = (0, len(A) - 1)
    current_k = None

    while interval[0] <= interval[1]:
        midpoint = (interval[0] + interval[1]) // 2

        if A[midpoint] < k:
            interval = (midpoint + 1, interval[1])
        else:  # if >= k
            if A[midpoint] == k:
                current_k = midpoint
            interval = (interval[0], midpoint - 1)

    if current_k is None:
        return -1

    return current_k


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", "search_first_key.tsv", search_first_of_k
        )
    )
