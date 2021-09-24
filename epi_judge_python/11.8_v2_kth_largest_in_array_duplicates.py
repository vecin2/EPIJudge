import heapq
from typing import List

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    left, right = 0, len(A) - 1

    while left <= right:
        pivot_index = (left + right) // 2
        index = partition(A, left, right, pivot_index)

        if index == k - 1:
            return A[index]
        elif index > k - 1:
            right = index - 1
        else:  # index < k-1
            left = index + 1

    return None


def partition(A: List[int], left, right, pivot_index):
    pivot = A[pivot_index]
    new_pivot_index = left
    A[right], A[pivot_index] = A[pivot_index], A[right]

    for i in range(left, right):
        if A[i] > pivot:
            A[i], A[new_pivot_index] = A[new_pivot_index], A[i]
            new_pivot_index += 1
    A[new_pivot_index], A[right] = A[right], A[new_pivot_index]

    return new_pivot_index


# 1 26 4 75 5 15 3


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "11.8_v2_kth_largest_in_array_duplicates.py",
            "11.8_v2_kth_largest_in_array_duplicates.tsv",
            find_kth_largest,
        )
    )
