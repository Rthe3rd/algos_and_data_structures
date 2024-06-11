# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # base cases: root is none
        # if root is None or p is None or q is None:
        #     return None
        # base cases based on root's value and sub nodes value
        # if root.val == p.val:
        #     return root
        # if root.val == q.val:
        #     return root
        # traverse the tree based on the roots val compared to the nodes
        curr = root
        while curr:
            if root.val < p.val and root.val < q.val:
                curr = curr.right
            elif root.val > p.val and root.val > q.val:
                curr = curr.left
            else:
                return curr