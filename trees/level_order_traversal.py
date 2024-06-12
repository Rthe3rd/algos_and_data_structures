# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return
        results = []
        current_level = [[root]]
        while current_level[0]:
            current_parents = current_level.pop(0)
            # maybe a while loop instead so you don't need to have a second array?
            child_holder = []
            for parent in current_parents:
                if parent.left:
                    child_holder.append(parent.left)
                if parent.right:
                    child_holder.append(parent.right)
            current_level.append(child_holder)
            # return the values
            results.append([parent.val for parent in current_parents])
        return results
    


    def level_Order(root):
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            q_length = len(q)
            level = []
            for i in range(q_length):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)