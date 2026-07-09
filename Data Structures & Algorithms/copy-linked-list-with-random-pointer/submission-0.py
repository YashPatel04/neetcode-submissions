"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return head
        oldToCopy = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr]=copy
            curr = curr.next
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next] if curr.next is not None else None
            copy.random = oldToCopy[curr.random] if curr.random is not None else None
            curr = curr.next
        return oldToCopy[head]
