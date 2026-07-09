class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        def build(left, right):
            if left>right: return None
            node = TreeNode(preorder[self.pre_idx])
            self.pre_idx+=1
            mid = hashmap[node.val]
            if mid>left:
                node.left = build(left, mid-1)
            if mid<right:
                node.right = build(mid+1, right)
            return node
        return build(0, len(preorder)-1)