import collections
import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class ResultStatus:
    def __init__(self, ancestor, no_found):
        self.ancestor = ancestor
        self.no_found = no_found


def lca(
    tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode
) -> Optional[BinaryTreeNode]:
    return lca_result(tree, node0, node1).ancestor


def lca_result(tree, node0, node1):
    if not tree:
        return ResultStatus(None, 0)

    left_result = lca_result(tree.left, node0, node1)

    if left_result.ancestor:
        return left_result

    right_result = lca_result(tree.right, node0, node1)

    if right_result.ancestor:
        return right_result

    nodes_found = (
        left_result.no_found
        + right_result.no_found
        + int(tree is node0)
        + int(tree is node1)
    )
    result = ResultStatus(tree if nodes_found == 2 else None, nodes_found)

    return result


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(
            lca, tree, must_find_node(tree, key1), must_find_node(tree, key2)
        )
    )

    if result is None:
        raise TestFailure("Result can't be None")

    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor.py", "lowest_common_ancestor.tsv", lca_wrapper
        )
    )
