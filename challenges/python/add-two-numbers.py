# Add two numbers, given as linkedlists with digits in reverse order. Return sum as linkedlist in reverse order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_string = ''
        while l1:
            l1_string = str(l1.val) + l1_string
            l1 = l1.next
        
        l2_string = ''
        while l2:
            l2_string = str(l2.val) + l2_string
            l2 = l2.next
            
        sum = int(l1_string) + int(l2_string)
        
        if sum == 0:
            return ListNode(0)
        
        head = None
        while sum > 0:
            digit = sum % 10
            if head == None:
                head = ListNode(digit)
                ptr = head
                head.next = None
            else:
                ptr.next = ListNode(digit)
                ptr = ptr.next
            sum //= 10
            
        return head
