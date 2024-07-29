# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_level_order(root):
    if not root:
        return ('empty')

    print(f'root: {root.val}')
    if root.right:
        print(f'root.right: {root.right.val}')
    if root.left:
        print(f'root.left: {root.left.val}')

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
        print('returning root!')
        return root
    

tree_root = TreeNode(1)
tree_root.left = TreeNode(3)


print_level_order(tree_root)
Solution().invert_bst(tree_root)
print_level_order(tree_root)
