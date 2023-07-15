# LC 234
# Palindrome Linked List
# Determine if linked list is a palindrome 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        return lst == lst[::-1]