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
            # print("popping", curr_node.val, level)
            
            if level > curr_level:
                curr_level = level
                output_list.append(list_for_level)
                list_for_level = []
            
            list_for_level.append(curr_node.val)
            
            if curr_node.left:
                # print("appending", curr_node.left.val, level+1)
                queue.append((curr_node.left, level+1))
            if curr_node.right:
                # print("appending", curr_node.right.val, level+1)
                queue.append((curr_node.right, level+1))
            
        output_list.append(list_for_level)
        return output_list
