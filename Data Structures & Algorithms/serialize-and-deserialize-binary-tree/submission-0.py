# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return "null"
        stack = deque()
        list = []
        stack.append(root)
        while stack:
            Rnode = stack.popleft()
            if not Rnode: 
                list.append("null")
                continue
            list.append(f"{Rnode.val}")
            stack.append(Rnode.left)
            stack.append(Rnode.right)
        while list and list[-1] == "null":
            list.pop()
        return ",".join(list)
        


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        list = deque(data.split(","))
        if list == [] or list[0]=="null": return None
        root= TreeNode(int(list.popleft()))
        nodes=deque()
        nodes.append(root)
        while nodes:
            node = nodes.popleft()
            if list: 
                t = list.popleft()
                if t != 'null':
                    node.left = TreeNode(int(t))
                    nodes.append(node.left)
            if list:
                t = list.popleft()
                if t != 'null': 
                    node.right = TreeNode(int(t))
                    nodes.append(node.right)
        return root
        
        
        


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))