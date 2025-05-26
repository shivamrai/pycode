"""LeetCode 100. Same Tree
https://leetcode.com/problems/same-tree/"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:  # Check if one of them is None
            return False
        if p.val != q.val:  # Check if values are different
            return False
        
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    

if __name__ == "__main__":
    # Example usage:
    # Constructing two binary trees:
    # Tree 1:       1
    #              / \
    #             2   3
    # Tree 2:       1
    #              / \
    #             2   3
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)

    solution = Solution()
    print(solution.isSameTree(root1, root2))  # Output: True