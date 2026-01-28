# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return
        q = []
        q.append(root)
        node = None
        result = []
        level = []
        while (q):
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if (node.left):
                    q.append(node.left)
                if (node.right):
                    q.append(node.right)
            result.append(level)
            level = []
        return result


if __name__ == '__main__':
    # TreeNode rootNode = TreeNode()
    # print(levelOrder(rootNode))
    pass
