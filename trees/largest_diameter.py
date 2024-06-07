class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):
        # The scope of variables requires this to be a mutable object
        largest_diameter = [0]

        def height(current_root):
            # Base Case: current_root is None -> return height of 0
            if current_root == None:
                return 0

            # calculate the height of the left and right nodes
            left_height = height(current_root.left)
            right_height = height(current_root.right)
            # calculate the current_diameter
            current_diameter = left_height + right_height
            # calculate the largest diamter
            largest_diameter[0] = max(largest_diameter[0], current_diameter)
            # calculate the height
            return 1 + max(left_height, right_height)
        # call the helper function
        height(root)
        # return the largest diameter
        return largest_diameter[0]