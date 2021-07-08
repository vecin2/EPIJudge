from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []
    nodes = []
    nodes.append(tree)
    result = []

    while nodes:

        result.append([node.data for node in nodes])

        nodes = compute_next_level(nodes)

    return result


def compute_next_level(nodes):
    return [child for node in nodes for child in (node.left, node.right) if child]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_level_order.py", "tree_level_order.tsv", binary_tree_depth_order
        )
    )
