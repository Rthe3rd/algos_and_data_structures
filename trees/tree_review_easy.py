# Review the leet code easy problems for trees
# 1. Invert Binary Tree
# 2. Maximim Depth of Binary Tree
# 3. Diameter of Binary Tree
# 4. Balanced Binary Tree
# 5. Same Tree
# 6. Subtree of another Tree

# 2. maxDepth
# Two ways to do this: Depth First Search and Level Order Traversal
def maxDepth(self, root):
    if root == None:
        # return None => correction: since we are wanting an integer at the end, we need to return an integer~ 
        return 0
    # If this method is within a class, don't for get to call self.maxDepth(root)
    return 1 + max(maxDepth(root.left), maxDepth(root.right)) 

# 1. Invert BT
def invertTree(self, root):
    if root == None:
        return None # Here we are not asking to return a value, but to modify the tree itself so no return value is needed
    # swap children
    temp = root.left
    root.left = root.right
    root.right = temp
    # invert the trees with roots at root.left and root.right
    invertTree(root.left)
    invertTree(root.right)
    # the final function call to be popped off of the callstack is the original function call with root
    return root

# 4. Balanced Tree
# Balanced tree means that there is not ever a time when the difference in height between and nodes is 1
def isBalanced(self, root):

    result = []
    def isBalanced_helper(root):
        if root == None:
            return [True, 0]
        
        left_height = isBalanced_helper(root.left)
        right_height = isBalanced_helper(root.right)

        # Determine if balanced
        balanced = (balanced and abs(left_height - right_height) >= 1)

        # calculate height
        height = 1 + left_height[1] + right_height[1]

        # return the results of the balanced and height calculations
        return result[balanced, height]

    return isBalanced_helper(root)[0]    