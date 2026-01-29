from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Function to print the tree in level order for verification
    @staticmethod
    def print_tree(node):
        if not node:
            return "None"
        return f"{node.val}, {TreeNode.print_tree(node.left)}, {TreeNode.print_tree(node.right)}"


class Solution:

    def helper(self, pre_start: int, in_start: int,
               in_end: int) -> Optional[TreeNode]:
        if pre_start >= len(preorder) or in_start > in_end:
            return None

        # Root value is the current element in preorder
        root_val = preorder[pre_start]
        root = TreeNode(root_val)

        # Find the index of the root in inorder
        root_index = inorder.index(root_val, in_start, in_end + 1)

        # Calculate the size of the left subtree
        left_size = root_index - in_start

        # Recursively build the left and right subtrees
        root.left = self.helper(pre_start + 1, in_start, root_index - 1)
        root.right = self.helper(
            pre_start + 1 + left_size,
            root_index + 1,
            in_end)

        return root

    def buildTree(
            self,
            preorder: list[int],
            inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # preorder is: root, left, right
        # inorder is: left, root, right
        return self.helper(0, 0, len(inorder) - 1)


if __name__ == "__main__":
    # Example usage:
    # Preorder: [3, 9, 20, 15, 7]
    # Inorder: [9, 3, 15, 20, 7]
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    # output = "3, 9, 20, None, None, 15,7

    solution = Solution()
    root = solution.buildTree(preorder, inorder)

    print(TreeNode.print_tree(root))
