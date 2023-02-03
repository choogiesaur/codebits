# LC 142
# find cycle in list, return node where it is located at
# do it by adding elements to set, check membership of each current node in the set
# first node that is found to be already in the set, is the cycle node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()

        while head:
            if head in s:
                return head
            s.add(head)
            head = head.next
        
        return None
