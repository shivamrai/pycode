"""Reverse Linked List - Reverse a linked list."""


# Definition for singly-linked list.
class ListNode:
    """ListNode class."""

    def __init__(self, x):
        """__init__ function."""
        self.val = x
        self.next = None


class Solution:
    """Solution class."""

    def reverse_list(self, head: ListNode) -> ListNode:
        """reverse_list function."""
        dummyNode = reversedList = ListNode(0)
        array = []
        while head:
            array.append(head.val)
            head = head.next
        array.reverse()
        for i in array:
            dummyNode.next = ListNode(i)
            dummyNode = dummyNode.next
        return reversedList.next
