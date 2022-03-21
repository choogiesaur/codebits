# BFS/Level Order Traversal:
# If not root, return
# Start with empty queue containing root
# While queue,
# Make empty level list
# Make

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = deque([root])
        output_list = []
        
        curr_level = 1
        
        while queue:
            level_list = []
            curr_len = len(queue)
            print(curr_level)
            
            for i in range(curr_len):
                popped = queue.popleft()
                if curr_level % 2 == 0:
                    level_list.insert(0, popped.val)
                else:
                    level_list.append(popped.val)
                
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
                    
            curr_level += 1
            output_list.append(level_list)
            
        return output_list
