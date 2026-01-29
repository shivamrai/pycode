"""Merge Sorted Lists - Merge two sorted linked lists."""


# Definition for singly-linked list.
class ListNode:
    """ListNode class."""

    def __init__(self, x):
        """__init__ function."""
        self.val = x
        self.next = None


class Solution:
    """Solution class."""

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """merge_two_lists function."""
        # dummy Node
        head = mergedSortedList = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                mergedSortedList.next = l1
                l1 = l1.next
                mergedSortedList = mergedSortedList.next
            else:
                mergedSortedList.next = l2
                l2 = l2.next
                mergedSortedList = mergedSortedList.next
        mergedSortedList.next = l1 or l2
        return head.next
