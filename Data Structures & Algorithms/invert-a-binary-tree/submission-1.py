# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return
            tr=root.right if root.right else None
            tl=root.left if root.left else None
            root.right=tl
            root.left=tr
            dfs(root.right)
            dfs(root.left)
            return
        dfs(root)
        return root