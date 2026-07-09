# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque()
        queue.append(root)
        list = []
        list.append([root.val])
        while queue:
            l = []
            n = len(queue)
            c=1
            while c<=n:
                node = queue.popleft()
                if node.left:
                    l.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    l.append(node.right.val)
                    queue.append(node.right)
                c+=1
            if len(l)>0: list.append(l)
        return list