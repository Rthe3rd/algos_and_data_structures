# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Return value (child to parent): boolean
        # State to pass (parent to child): What is required to validate a BST -> min/max value seen
      def helper(root, min_value_seen, max_value_seen):
        # If you have an empty tree or have reached the bottom of the tree
        if not root:
          return True

        # Compare current root to the min/max value seen NOT children
        # The less than or equal to/greater than or equal to is needed IF you want to use this boolean in order to catch nodes that are the same equal in val 
        if root.val <= min_value_seen or root.val >= max_value_seen:
          return False

        return helper(root.left, min_value_seen = min_value_seen, max_value_seen = root.val) and helper(root.right, min_value_seen = root.val, max_value_seen = max_value_seen)
        # Base case: if you have an empty  or at the bottom of the tree
    
      return helper(root, float("-inf"), float("inf"))