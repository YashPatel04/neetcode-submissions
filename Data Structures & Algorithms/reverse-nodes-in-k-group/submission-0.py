# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, k):
        prev, curr = None, head
        while curr and k>0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            k-=1
        return prev

    def getKth(self, curr, k):
        while k>0:
            curr = curr.next if curr else None
            k-=1
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        prev = dummy
        while True:
            kth = self.getKth(prev, k)
            if not kth: break
            nxt = kth.next
            temp = prev.next
            prev.next = self.reverse(curr, k)
            temp.next = nxt
            prev = temp
            curr = prev.next
        return dummy.next

