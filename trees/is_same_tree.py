class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        is_balanced = [True]

        def is_same_tree_helper(current_p, current_q):
            if not current_p and not current_q:
                return is_balanced
            # if (not current_p and current_q) or (current_p and not current_q):
            if not current_p or not current_q:
                is_balanced[0] = False
                return is_balanced
            if current_p.val != current_q.val:
                is_balanced[0] = False
                return is_balanced
            return is_same_tree_helper(current_p.right, current_q.right) and is_same_tree_helper(current_p.left, current_q.left)

        is_same_tree_helper(p,q)

        return is_balanced[0]

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        current_p, current_q = p, q
        if not current_p and not current_q:
            return True
        if not current_p or not current_q or current_p.val != current_q.val:
            return False
        return self.isSameTree(current_p.right, current_q.right) and self.isSameTree(current_p.left, current_q.left)