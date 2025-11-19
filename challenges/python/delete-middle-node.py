# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        count = 1
        ptr = head
        while ptr.next:
            count += 1
            ptr = ptr.next

        # print(count//2) 

        ptr = head
        for i in range(count//2-1):
            ptr = ptr.next

        # snip that badboy out
        ptr.next = ptr.next.next
        return head
