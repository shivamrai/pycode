from typing import Optional
# """LeetCode 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left  # Swap left and right children
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    def invertTreeOptional(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Preorder traversal to invert the tree
        def preorder_invert(node: Optional[TreeNode]):
            if not node:
                return
            # Swap left and right children
            node.left, node.right = node.right, node.left
            preorder_invert(node.left)
            preorder_invert(node.right)

        preorder_invert(root)
        return root

    # Serialize the tree in inorder traversal
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result
    
if __name__ == "__main__":
    # Example usage:
    # Constructing a binary tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    inverted_root = solution.invertTree(root)

    # Function to print the tree in pre-order for verification
    def print_tree(node):
        if not node:
            return
        print(node.val, end=' ')
        print_tree(node.left)
        print_tree(node.right)

    print_tree(inverted_root)  # Output: 1 3 2 5 4