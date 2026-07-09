# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size+=1
            curr = curr.next
        i = -1
        curr = ListNode()
        curr.next = head
        while i<size:
            if (i+1)==(size-n):
                if curr.next == head:
                    head = curr.next.next
                    break
                curr.next = curr.next.next if curr.next else None
                break
            curr = curr.next
            i+=1
        return head