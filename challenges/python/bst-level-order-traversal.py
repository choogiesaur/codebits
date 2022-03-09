# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        curr_level = 0
        queue = deque([(root, curr_level)])
        output_list = []
        
        # Sublist for elements of a single level
        list_for_level = []
        
        while queue:
            
            (curr_node, level) = queue.popleft()
            
            # If level of popped node is greater than curr level, we've reached next level in queue
            if level > curr_level:
                curr_level = level
                # Put it in output and start new level list
                output_list.append(list_for_level)
                list_for_level = []
            
            list_for_level.append(curr_node.val)
            
            # Enqueue its children
            if curr_node.left:
                queue.append((curr_node.left, level+1))
            if curr_node.right:
                queue.append((curr_node.right, level+1))
                
        # Can I eliminate having to append one last time?    
        output_list.append(list_for_level)
        return output_list
