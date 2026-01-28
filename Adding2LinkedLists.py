# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        linkedListSum = None
        first = None
        while l1 or l2 or carry:
            # calculcate sum of digits
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
                linkedListSum.next = ListNode(value)
                linkedListSum = linkedListSum.next
            else:
                linkedListSum = ListNode(value)
                first = linkedListSum

            # move to next digits
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return first
