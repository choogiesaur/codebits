# Input: root = [3,9,20,null,null,15,7]
# Output: 3
def maxDepth(self, root: TreeNode) -> int:
  
    # Visit root; if none, no extra depth discovered
    if root == None:
        return 0
      
    # If not none; max depth is 1 extra level discovered + max of left and right subtrees
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)
    return 1 + max(left, right)
