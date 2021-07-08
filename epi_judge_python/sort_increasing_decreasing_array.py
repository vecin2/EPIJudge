from typing import List

from sorted_arrays_merge import merge_sorted_arrays
from test_framework import generic_test


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    # convert A to list of increasing and decreasing arrays
    sorted_arrays = split(A)

    return merge_sorted_arrays(sorted_arrays)


INCREASING, DECREASING = 0, 1


def split(A):
    tendency = INCREASING

    sorted_arrays = []
    current_arr = [A[0]]

    for index in range(1, len(A)):
        value = A[index]

        if continues_tendency(A, index, tendency):
            current_arr.append(value)

        else:
            sorted_arrays.append(current_arr)
            current_arr = [value]

            if tendency == DECREASING:
                tendency = INCREASING
                current_arr.reverse()

    if tendency == DECREASING:
        current_arr.reverse()
    sorted_arrays.append(current_arr)

    return sorted_arrays


def continues_tendency(A, index, tendency):
    value = A[index]

    return (value >= A[index - 1] and tendency == INCREASING) or (
        value <= A[index - 1] and tendency == DECREASING
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_increasing_decreasing_array.py",
            "sort_increasing_decreasing_array.tsv",
            sort_k_increasing_decreasing_array,
        )
    )
