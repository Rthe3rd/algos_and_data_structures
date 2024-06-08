# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def max_depth(current_root):
            if current_root == None:
                return [True, 0]
            
            right_height = max_depth(current_root.right)
            left_height = max_depth(current_root.left)
            balanced = (right_height[0] and left_height[0] and abs(left_height[1] - right_height[1]) <= 1)
            return [balanced, 1 + max(right_height[1], left_height[1])]
        
        return max_depth(root)[0]