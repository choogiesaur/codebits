# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode()
        even_head = ListNode()
        
        counter = 1
        odd_ptr = odd_head
        even_ptr = even_head
        while head:
            if counter % 2 == 1:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
            else:
                even_ptr.next = head
                even_ptr = even_ptr.next
            counter += 1
            head = head.next
        
        # prevent cycle by setting end's next to None
        even_ptr.next = None
        odd_ptr.next = even_head.next
        return odd_head.next