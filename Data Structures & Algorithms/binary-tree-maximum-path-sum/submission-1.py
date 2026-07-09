# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def calcMax(node):
            if not node: return 0
            temp = node.val
            leftMax = max(0, calcMax(node.left))
            rightMax = max(0, calcMax(node.right))
            self.res = max(self.res, temp+leftMax+rightMax)
            return max(temp+leftMax, temp+rightMax)
        calcMax(root)
        return self.res