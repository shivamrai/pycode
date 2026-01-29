"""Construct Binary Tree - Build tree from traversals."""

from typing import Optional


class TreeNode:
    """TreeNode class."""

    def __init__(self, val=0, left=None, right=None):
        """__init__ function."""
        self.val = val
        self.left = left
        self.right = right

    # Function to print the tree in level order for verification
    @staticmethod
    def print_tree(node):
        """print_tree function."""
        if not node:
            return "None"
        return f"{node.val}, {TreeNode.print_tree(node.left)}, {TreeNode.print_tree(node.right)}"


class Solution:
    """Solution class."""

    def __init__(self):
        """Initialize solution with empty preorder and inorder lists."""
        self.preorder = []
        self.inorder = []

    def helper(self, pre_start: int, in_start: int, in_end: int) -> Optional[TreeNode]:
        """Helper function to construct tree from preorder and inorder."""
        if pre_start >= len(self.preorder) or in_start > in_end:
            return None

        # Root value is the current element in preorder
        root_val = self.preorder[pre_start]
        root_node = TreeNode(root_val)

        # Find the index of the root in inorder
        root_index = self.inorder.index(root_val, in_start, in_end + 1)

        # Calculate the size of the left subtree
        left_size = root_index - in_start

        # Recursively build the left and right subtrees
        root_node.left = self.helper(pre_start + 1, in_start, root_index - 1)
        root_node.right = self.helper(
            pre_start + 1 + left_size,
            root_index + 1,
            in_end)

        return root_node

    def build_tree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """Build tree from preorder and inorder traversals."""
        if not preorder or not inorder:
            return None
        # preorder is: root, left, right
        # inorder is: left, root, right
        self.preorder = preorder
        self.inorder = inorder
        return self.helper(0, 0, len(inorder) - 1)


if __name__ == "__main__":
    # Example usage:
    # Preorder: [3, 9, 20, 15, 7]
    # Inorder: [9, 3, 15, 20, 7]
    test_preorder = [3, 9, 20, 15, 7]
    test_inorder = [9, 3, 15, 20, 7]
    # output = "3, 9, 20, None, None, 15,7

    solution = Solution()
    root = solution.build_tree(test_preorder, test_inorder)

    print(TreeNode.print_tree(root))
