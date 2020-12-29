
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        head.next = None
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        dummy = self.head
        len = 0
        while(dummy):
            dummy = dummy.next
            len+=1
        rRange = random.randint(0,len-1)
        for i in range(0,rRange-1):
            self.head = self.head.next
        if(self.head):
            return self.head.val
        else:
            return -1

if __name__ == "__main__":
    #Init a singly linked list [1,2,3].
    ListNode dead = new ListNode(1);
    head.next = new ListNode(2);
    head.next.next = new ListNode(3);
    Solution solution = new Solution(head);
