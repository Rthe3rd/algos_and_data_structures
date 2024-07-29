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
            # Once you have found the bottom node/leaf, or an empty tree, return true and a height of 0
            if current_root == None:
                return [True, 0]
            # calculate the right height
            right_height = max_depth(current_root.right)
            # calculate the left height
            left_height = max_depth(current_root.left)
            # boolean value that checks previous left AND previous right booleans AND the differences in left/right heights
            balanced = (right_height[0] and left_height[0] and abs(left_height[1] - right_height[1]) <= 1)
            # return the array holding the boolean and the total current height at the current node/leaf
            return [balanced, 1 + max(right_height[1], left_height[1])]
        # return just the boolean in the end from the method call with the root as its arguement 
        return max_depth(root)[0]