# Gitting Gud at Iterative Dfs
# Empty stack, curr = root
# While stack not empty or there is a curr,
# Iterate down-left while pushing all to stack, exiting when cant go further
# Pop from stack and visit that node
# Set curr to popped node's right...allows us to attempt leftward descent on the right subtree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = deque([])
        curr = root
        
        return_next_node = False
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            popped = stack.pop()
            if return_next_node == True:
                return popped
            if popped == p:
                return_next_node = True
            
            if popped.right:
                curr = popped.right
