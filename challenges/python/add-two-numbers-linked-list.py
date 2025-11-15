# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # process l1
        l1_sum = 0
        multiplier = 1
        while l1:
            l1_sum += l1.val * multiplier
            multiplier *= 10
            l1 = l1.next
        
        #process l2
        l2_sum = 0
        multiplier = 1
        while l2:
            l2_sum += l2.val * multiplier
            multiplier *= 10
            l2 = l2.next
            
        total = l1_sum + l2_sum
        head = ListNode()
        multiplier = 1
        
        if total == 0:
            return ListNode()
        
        curr = head
        while total != 0:
            digit = total % 10
            curr.next = ListNode(digit)
            curr = curr.next
            total //= 10
        
        # first head was dummy, its next is the first true node
        return head.next
        