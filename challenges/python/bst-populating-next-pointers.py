"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None
        
        def bfs(root):
            # deque() constructor takes a list of items to start the queue
            queue = deque([root])
            
            while queue:
                
                curr_len = len(queue)
                for i in range(curr_len):
                    curr = queue.popleft()
                    
                    if i == curr_len - 1:
                        curr.next = None
                    else:
                        curr.next = queue[0]
                    
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            
            return root
        
        return bfs(root)
