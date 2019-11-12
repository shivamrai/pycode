Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #dummy Node
        head = mergedSortedList = ListNode(0)
        while (l1 and l2):
            if(l1.val<l2.val):
                mergedSortedList.next = l1
                l1 = l1.next
                mergedSortedList = mergedSortedList.next
            else:
                mergedSortedList.next = l2
                l2 = l2.next
                mergedSortedList = mergedSortedList.next
        mergedSortedList.next = l1 or l2
        return head.next