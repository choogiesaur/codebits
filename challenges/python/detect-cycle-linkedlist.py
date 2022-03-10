"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

# Could also put hard limit on nodes searched to x, if there is such a constraint x on size of linkedlist
def has_cycle(head):
    observed_values = set()

    curr = head
    while curr:
        if curr in observed_values:
            return True
        observed_values.add(curr)
        curr = curr.next
    return False
