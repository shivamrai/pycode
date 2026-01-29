"""Add Two Numbers - Sum two linked lists representing numbers in reverse order.

LeetCode 2: Add two non-negative integers represented as linked lists in reverse order.
"""

# Definition for singly-linked list.
class ListNode:
    """Node in a singly linked list."""

    def __init__(self, x):
        """Initialize a node with value x."""
        self.val = x
        self.next = None


class Solution:
    """Solution for Add Two Numbers problem."""

    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add two numbers represented as linked lists.

        Args:
            l1: First linked list (reversed digits).
            l2: Second linked list (reversed digits).

        Returns:
            A linked list representing the sum (in reverse order).
        """
        carry = 0
        linked_list_sum = None
        first = None
        while l1 or l2 or carry:
            # calculate sum of digits
            value = 0
            if l1:
                value += l1.val
            if l2:
                value += l2.val
            value += carry
            if value > 9:
                carry = 1
                value -= 10
            else:
                carry = 0

            # add new node
            if first:
                linked_list_sum.next = ListNode(value)
                linked_list_sum = linked_list_sum.next
            else:
                linked_list_sum = ListNode(value)
                first = linked_list_sum

            # move to next digits
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return first
