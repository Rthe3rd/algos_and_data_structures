class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: None, val: int):
        # This base case is when you either have an empty tree or have reached the end of the tree
        if not root:
            return TreeNode(val)

        # The state passed is the val you are comparing at each node and the next node root.left/right
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        return root
