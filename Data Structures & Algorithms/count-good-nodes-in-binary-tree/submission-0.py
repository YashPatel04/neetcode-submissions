# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    good = 0
    def goodNodes(self, root: TreeNode) -> int:
        def check(node, maximum):
            if not node: return
            if node.val>=maximum:
                maximum = node.val
                self.good+=1
            check(node.left, maximum)
            check(node.right, maximum)
        check(root, root.val)
        return self.good
