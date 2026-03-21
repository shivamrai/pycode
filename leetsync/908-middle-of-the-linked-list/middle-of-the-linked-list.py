from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_ptr, fast_ptr = head, head
        while fast_ptr and fast_ptr.next:
            if slow_ptr is not None:  # Type guard
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
        return slow_ptr
