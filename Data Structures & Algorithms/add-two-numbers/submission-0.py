# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        A, B = l1, l2
        dummy = ListNode()
        curr = dummy
        carry = 0
        while A or B:
            t = ListNode()
            curr.next = t
            curr = t
            valA = A.val if A else 0
            valB = B.val if B else 0

            val = valA + valB + carry
            if val>=10:
                carry = 1
                val = val%10
            else:
                carry = 0
            curr.val = val
            A = A.next if A else None
            B = B.next if B else None
        if carry == 1:
            t = ListNode(1,None)
            curr.next = t
        return dummy.next