# LC 206

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None

        new_head = None

        ptr = head
        while ptr:
            temp = ptr.next
            if new_head == None:
                new_head = head
                new_head.next = None
                ptr = temp
            else:
                ptr.next = new_head
                new_head = ptr
                ptr = temp

        return new_head
