"""Random Node from Linked List - Return random node."""

import random

# Definition for singly-linked list.


class ListNode:
    """ListNode class."""

    def __init__(self, val=0, next_node=None):
        """__init__ function."""
        self.val = val
        self.next_node = next_node


class Solution:
    """Solution class."""

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        head.next_node = None

    def get_random(self) -> int:
        """
        Returns a random node's value.
        """
        dummy = self.head
        length = 0
        while dummy:
            dummy = dummy.next
            length += 1
        rRange = random.randint(0, length - 1)
        for _ in range(0, rRange - 1):
            self.head = self.head.next
        if self.head:
            return self.head.val
        return -1


if __name__ == "__main__":
    # Init a singly linked list [1,2,3].
    # dead = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # solution = Solution(head)
    pass
