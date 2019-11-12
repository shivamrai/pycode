#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummyNode = reversedList = ListNode(0)
        array = []
        while(head):
            array.append(head.val)
            head = head.next
        array.reverse()
        for i in array:
            dummyNode.next = ListNode(i)
            dummyNode = dummyNode.next
        return reversedList.next