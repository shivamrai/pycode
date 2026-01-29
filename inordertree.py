"""Level Order Tree Traversal - Traverse tree by levels."""


# Definition for a binary tree node.
class TreeNode:
    """TreeNode class."""

    def __init__(self, val=0, left=None, right=None):
        """__init__ function."""
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solution class."""

    def level_order(self, root: TreeNode):
        """level_order function."""
        if root is None:
            return []
        q = []
        q.append(root)
        result = []
        level = []
        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
            level = []
        return result


if __name__ == "__main__":
    # TreeNode rootNode = TreeNode()
    # print(level_order(rootNode))
    pass
