# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invert_bst(self, root):
        # base case
        if root == None:
            return None
        # temp swap left and right
        temp = root.left
        root.left = root.right
        root.right = temp
        # recursively call invert_bst
        self.invert_bst(root.left)
        self.invert_bst(root.right)
        # return root
        return root