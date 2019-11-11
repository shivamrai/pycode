# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.head = None
        
    def reverse(self, l1: ListNode): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        carry = 0
        sumofl1Andl2CurrentNode = 0
        numberString = 
        while l1 & l2:
            sumofl1Andl2CurrentNode = l1.val + l2.val + carry
            carry = sumofl1Andl2CurrentNode/10
            l3.val = sumofl1Andl2CurrentNode%10
            l1 = l1.next
            l2 = l2.next
        self.reverse(l3)
        while l3:
            
            