import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


########################### One hour once known#######################
# 2 -> 3 -> 4 >
#             5 -> 6
#     22-> 25>
#
#
# count element in lists
# move pointer forward in longer list as many elements as size different
#
# move both points until they are the same of the lists are finish
def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    rc0, rc1 = root_cycle(l0), root_cycle(l1)

    if not rc0 and not rc1:
        return overlapping_no_cycle_lists(l0, l1)

    if rc0 and rc1 and rc0 is not rc1:  # no merge or merge in cycle
        return overlap_in_cycle(rc0, rc1)

    elif rc0 and rc1:  # merge at root cycle or before
        next_rc0, next_rc1 = rc0.next, rc1.next
        rc0.next = rc1.next = None
        overlap_node = overlapping_no_cycle_lists(l0, l1)
        rc0.next, rc1.next = next_rc0, next_rc1

        return overlap_node

    return None


def overlap_in_cycle(rc0, rc1):
    loop = rc0.next

    while loop is not rc0:
        if loop is rc1:  # merge in cycle
            return loop
        loop = loop.next

    return None


def root_cycle(listnode):
    fast = ListNode(None, listnode)
    slow = ListNode(None, listnode)

    while fast and fast.next and fast is not slow:
        fast = fast.next.next
        slow = slow.next

    if fast is slow:
        start = ListNode(None, listnode)

        while start is not fast:
            start = start.next
            fast = fast.next

        return start

    return None


def overlapping_no_cycle_lists(l0, l1):
    l0_size = list_size(l0)
    l1_size = list_size(l1)

    if l0_size > l1_size:
        l0 = kth_elem(l0, l0_size - l1_size)
    else:
        l1 = kth_elem(l1, l1_size - l0_size)

    while l0:
        if l0 == l1:
            return l0
        l0, l1 = l0.next, l1.next

    return None


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
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0

            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1

            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0

        while last.next:
            last = last.next
        it = l0

        for _ in range(cycle0):
            if not it:
                raise RuntimeError("Invalid input data")
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1

        while last.next:
            last = last.next
        it = l1

        for _ in range(cycle1):
            if not it:
                raise RuntimeError("Invalid input data")
            it = it.next
        last.next = it

    common_nodes = set()
    it = common

    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure("Invalid result")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "do_lists_overlap.py", "do_lists_overlap.tsv", overlapping_lists_wrapper
        )
    )
