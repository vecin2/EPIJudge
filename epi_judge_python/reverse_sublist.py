from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    head_sublist = head = ListNode()
    head_sublist.next = L
    head.next = L

    for _ in range(1, start):
        head_sublist = head_sublist.next

    if head_sublist.next:
        reversed_sublist = reverse_at_front(head_sublist.next, finish - start)
        head_sublist.next = reversed_sublist

    return head.next


def reverse_at_front(L, top_index):
    prev = current = L
    current = current.next

    for _ in range(0, top_index):
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    L.next = current  # point the initial first element to the element after last

    return prev


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_sublist.py", "reverse_sublist.tsv", reverse_sublist
        )
    )
