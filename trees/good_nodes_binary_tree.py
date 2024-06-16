# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root, lower_bound = float('-inf'), upper_bound = float("inf")):
            # base case: if root == None: return True
            if not root:
                return True
            # conditions to check for validity
            if not(root.val > lower_bound and root.val < upper_bound):
                return False 

            # is_left_subTree/is_right_subTree 
            is_left_subTree = helper(root.left, lower_bound, root.val)
            is_right_subTree = helper(root.right, root.val, upper_bound)
            
            # return is_left_subTree and is_right_subTree 
            return (is_left_subTree and is_right_subTree) 

        return helper(root)