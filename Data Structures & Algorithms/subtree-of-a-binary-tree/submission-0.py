# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        def isSameTree(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val==q.val:
                return (isSameTree(p.left, q.left) and 
                    isSameTree(p.right, q.right))
            else:
                return False
        return (isSameTree(root, subRoot) or self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot))

