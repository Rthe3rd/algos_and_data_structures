def searchBST(self, root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    if not root:
        return
    if root.val == val:
        return root
    if root.val < val:
        return self.searchBST(root.right, val)
    if root.val > val:
        return self.searchBST(root.left, val)