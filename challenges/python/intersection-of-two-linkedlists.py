# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # First solution; Keep track of encountered values in hash set, once we see one we've already encountered:
    # Start a cycle detection process from there: iterate forward and if any reference is same as starting point, there is a cycle
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        b_visited = set()
        
        head = headB
        while head:
            b_visited.add(head)
            head = head.next
            
        head = headA
        while head:
            if head in b_visited:
                return head
            head = head.next
        
        return None
    # Faster solution: Traverse both linkedlists at same time. When one pointer ends, set it to head of other list.
    # Loop while pointers not equal. They will eventually land on the same node - the merge point - or the ends of both lists - Null/none.
    def getIntersectionNode_faster(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        
        ptr_a = headA
        ptr_b = headB
        
        while ptr_a != ptr_b:
            if ptr_a == None:
                ptr_a = headB
            else:
                ptr_a = ptr_a.next
                
            if ptr_b == None:
                ptr_b = headA
            else:
                ptr_b = ptr_b.next
        
        return ptr_a
