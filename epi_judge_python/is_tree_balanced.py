from collections import namedtuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

ResultCode = namedtuple("ResultCode", ("height", "is_balanced"))


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return balanced(tree).is_balanced


def balanced(node):
    if not node:
        return ResultCode(-1, True)

    left_result = balanced(node.left)

    if not left_result.is_balanced:
        return ResultCode(left_result.height + 1, False)

    right_result = balanced(node.right)

    if not right_result.is_balanced:
        return ResultCode(right_result.height + 1, False)

    return ResultCode(
        max(left_result.height, right_result.height) + 1,
        abs(left_result.height - right_result.height) <= 1,
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_balanced.py", "is_tree_balanced.tsv", is_balanced_binary_tree
        )
    )
