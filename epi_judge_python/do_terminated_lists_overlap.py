import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    l0_size = list_size(l0)
    l1_size = list_size(l1)

    if l0_size > l1_size:
        l0 = kth_elem(l0, l0_size - l1_size)  # advancing through l0
    else:
        l1 = kth_elem(l1, l1_size - l0_size)  # advancing through l1

    while l0 and l1 and l0 is not l1:  # l1 and l0 are now the same size
        l0, l1 = l0.next, l1.next

    return l0


def kth_elem(node, k):
    for _ in range(k):
        node = node.next

    return node


def list_size(l0):
    counter = 0

    while l0:
        counter += 1
        l0 = l0.next

    return counter


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0

            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1

            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure("Invalid result")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "do_terminated_lists_overlap.py",
            "do_terminated_lists_overlap.tsv",
            overlapping_no_cycle_lists_wrapper,
        )
    )
