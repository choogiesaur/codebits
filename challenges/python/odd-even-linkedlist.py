# LC 328

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        odd_head = None
        odd_ptr = None
        even_head = None
        even_ptr = None

        i = 1
        while head:

            # Odd index...
            if i % 2 != 0:
                if not odd_head:
                    odd_head = head
                    odd_ptr = odd_head
                else:
                    odd_ptr.next = head
                    odd_ptr = head
            # Even index...
            else:
                if not even_head:
                    even_head = head
                    even_ptr = even_head
                else:
                    even_ptr.next = head
                    even_ptr = head

            i += 1
            head = head.next

        # No odd list; Input was of zero length
        if not odd_head:
            return None
        else:
            # No more nodes after even_ptr, so tail it with None
            if even_ptr:
                even_ptr.next = None
            # Connect odd list tail to even list head
            odd_ptr.next = even_head
            return odd_head

# 3/20/2022 Solution
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
