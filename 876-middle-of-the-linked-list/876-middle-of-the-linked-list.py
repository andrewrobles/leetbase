# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, middle = head, 0
        while curr is not None:
            curr = curr.next
            middle += 1
        curr = head
        middle //= 2
        for _ in range(middle):
            curr = curr.next
        return curr
            
        