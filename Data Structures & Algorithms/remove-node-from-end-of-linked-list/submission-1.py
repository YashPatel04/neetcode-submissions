# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        target=0
        count=0
        dummy=head
        while dummy:
            dummy=dummy.next
            target+=1
        dummy=ListNode()
        target-=n
        curr=head
        dummy.next=curr
        if target==0:
            curr=curr.next
            dummy.next=curr
            count+=1
        while curr:
            if(count==target-1):
                curr.next=curr.next.next if curr.next is not None else None
            else:
                curr=curr.next
            count+=1
        return dummy.next