"""Maximum Depth Binary Tree - Find maximum depth of tree."""


class TreeNode:
    """TreeNode class."""

    def __init__(self, val=0, left=None, right=None):
        """__init__ function."""
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solution class."""

    def max_depth(self, root: 'TreeNode') -> int:
        """max_depth function."""
        if not root:
            return 0
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)
        return max(left_depth, right_depth) + 1


if __name__ == "__main__":
    # Example usage:
    # Constructing a binary tree:
    #       1
    #      / \
    #     2   3
    #    /
    #   4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    solution = Solution()
    print(solution.max_depth(root))  # Output: 3
