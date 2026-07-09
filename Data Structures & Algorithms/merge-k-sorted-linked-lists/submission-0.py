# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists)>1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1<len(lists) else None
                mergedLists.append(self.mergeLists(l1,l2))
            lists = mergedLists
        return lists[0]

    def mergeLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1

        dummy = ListNode()
        head = dummy
        while l1 and l2:
            if(l2.val<l1.val):
                node = ListNode(l2.val)
                dummy.next = node
                l2 = l2.next
            else:
                node = ListNode(l1.val)
                dummy.next = node
                l1 = l1.next
            dummy = dummy.next
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        return head.next