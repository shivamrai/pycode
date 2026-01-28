class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False

        return (
            t1.val == t2.val
            and self.isMirror(t1.left, t2.right)
            and self.isMirror(t1.right, t2.left)
        )  # Check if the values are equal and recursively check left and right subtrees

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)


if __name__ == "__main__":
    # Example usage:
    # Constructing a symmetric binary tree:
    #       1
    #      / \
    #     2   2
    #    / \ / \
    #   3  4 4  3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    solution = Solution()
    print(solution.isSymmetric(root))  # Output: True
