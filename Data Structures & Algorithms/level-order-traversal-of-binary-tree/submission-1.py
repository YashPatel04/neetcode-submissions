# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l=[]
        def levelOrder(node, level, l):
            if not node:
                return 
            if level==len(l):
                l.append([])
            l[level].append(node.val)
            levelOrder(node.left, level+1, l)
            levelOrder(node.right, level+1, l)
        levelOrder(root,0,l)
        return l