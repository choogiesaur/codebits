# Given a BST, return Kth smallest element
# Do inorder traversal, return the kth element visited

# Again for iterative inorder DFS:
# Empty stack, curr = root
# While stack or curr:
# Iterate downleft, pushing everything to stack along the way but not visiting
# When you cant iterate left any more...pop and visit
# Set curr equal to popped node's right, to attempt leftward traversal of right subtree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        
        stack = deque([])
        curr = root
        
        num_visited = 0
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            popped = stack.pop()
            num_visited += 1
            if num_visited == k:
                return popped.val
            
            curr = popped.right
