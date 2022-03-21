# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return 
        if not head.next:
            return head
        
        odd_ptr = head
        even_head = head.next
        even_ptr = even_head
        
        while even_ptr and even_ptr.next:
            # Add next odd to odd list, increment odd pointer
            odd_ptr.next = even_ptr.next
            odd_ptr = odd_ptr.next
            # Add next even to list; either a real even, or None, which is okay since end of Even list should point to None
            even_ptr.next = odd_ptr.next
            even_ptr = even_ptr.next
            
        odd_ptr.next = even_head
        return head
