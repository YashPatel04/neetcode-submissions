# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, level):
        if not node:
            return level
        return max(self.dfs(node.right, level+1), self.dfs(node.left, level+1))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
