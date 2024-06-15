# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        nodes_seen = []
        nodes_in_order = []

        def helper(current_root):
            if current_root is None:
                return
            nodes_seen.append(current_root)
            helper(current_root.left)
            nodes_in_order.append(nodes_seen.pop())
            helper(current_root.right)
            return nodes_in_order
        
        return helper(root)[k-1].val