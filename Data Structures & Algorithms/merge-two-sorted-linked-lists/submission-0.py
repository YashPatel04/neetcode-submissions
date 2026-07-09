# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        A, B = list1, list2
        h = ListNode()
        prev = h
    
        while(A and B):
            if A.val < B.val:
                prev.next = A
                prev = A
                A = A.next
            else:
                prev.next = B
                prev = B
                B = B.next
        if A:
            prev.next = A
        if B:
            prev.next = B  
        return (h.next) 
