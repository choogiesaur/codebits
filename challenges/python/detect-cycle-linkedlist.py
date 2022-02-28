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

    while head:
        # If we've seen this value before, start cycle search mode
        if head.data in observed_values:
            temp = head
            while temp:
                # From duplicate value node traverse further, if any reference equals the branching point, there is a cycle
                if(temp is head):
                    return True
                temp = temp.next
        # Add current node to list of observed
        observed_values.add(head.data)
        head = head.next
    
    return False
