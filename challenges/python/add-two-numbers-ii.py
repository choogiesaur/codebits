# Lists are in regular order, not reversed
# Lists can be different size
# instead of str conversion:
# Calculate MSD with: total = total*10 + current_digit
# on next pass, multiply by 10 and add current digit,
# so on and you will have total

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_string = ''
        while l1:
            l1_string += str(l1.val) 
            l1 = l1.next
        
        l2_string = ''
        while l2:
            l2_string += str(l2.val)
            l2 = l2.next
            
        sum = int(l1_string) + int(l2_string)
        
        if sum == 0:
            return ListNode(0)
        
        # The first head will ultimately be the tail
        head = None
        while sum > 0:
            digit = sum % 10
            if head == None:
                head = ListNode(digit)
            else:
                temp = ListNode(digit, head)
                head = temp
            sum //= 10
            
        return head
