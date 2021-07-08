from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    result = []

    if n > 0:
        result.append([1])

    for i in range(1, n):
        result.append([1])

        for j in range(1, i):
            pascal_no = result[i - 1][j - 1] + result[i - 1][j]
            result[-1].append(pascal_no)
        result[-1].append(1)

    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "pascal_triangle.py", "pascal_triangle.tsv", generate_pascal_triangle
        )
    )
