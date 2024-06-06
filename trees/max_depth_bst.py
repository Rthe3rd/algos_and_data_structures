# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


    def maxDepth_level_order_traversal(self, root):

        if not root:
            return 0

        level = 0
        queue = [root]

        while queue:
            for i in range(len(queue)):
                current_root = queue.pop(0)
                if current_root.left:
                    queue.append(current_root.left)
                if current_root.right:
                    queue.append(current_root.right)
            level += 1
        return level
