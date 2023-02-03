# LC 21

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        new_head = None

        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        # Pick head of new list
        if list1.val < list2.val:
            new_head = list1
            list1 = list1.next
        else:
            new_head = list2
            list2 = list2.next

        ptr = new_head
        while list1 or list2:
            if not list1:
                ptr.next = list2
                break
            elif not list2:
                ptr.next = list1
                break
            elif list1.val < list2.val:
                ptr.next = list1
                ptr = ptr.next
                list1 = list1.next
            else:
                ptr.next = list2
                ptr = ptr.next
                list2 = list2.next
        
        return new_head
