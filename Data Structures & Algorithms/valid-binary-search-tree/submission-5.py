# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, lower, upper, node):
        if not node:
            return True

        if not (lower < node.val < upper):
            return False

        return (
            self.dfs(lower, node.val, node.left) and
            self.dfs(node.val, upper, node.right)
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(float('-inf'), float('inf'), root)
