# Review the leet code problems for trees
# 1. Invert Binary Tree
# 2. Maximim Depth of Binary Tree
# 3. Diameter of Binary Tree
# 4. Balanced Binary Tree
# 5. Same Tree
# 6. Subtree of another Tree

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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

# 6. Subtree of Another Tree
def isSubtree(self, root, subRoot):
    if not subRoot:
        return True
    if not root:
        return False
    # Are they the same tree? First time checks to see if root and subRoot are the same. 
    # Subsequent calls from the subsequent recursive calls check to see if the left/right sides contains the subRoot, recursively
    if self.isSameTree(root, subRoot): 
        return True
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 

def isSameTree(self, root, subRoot):
    if root == None and subRoot == None:
        return True
    if root == None and subRoot != None or root != None and subRoot == None or root.val != subRoot.val:
        return False
    return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)

# 3. Max Diamter

def maxDiameter(self, root):
    max_diameter = [0] 
    def height(root):
        # If you reach the bottom, return 0
        if root == None:
            return 0
        
        # calculate the HIEGHT of the current root with the respective left and right heights
        left_height = height(root.left)
        right_height = height(root.right)
        
        # calculate the diameter of the current node
        current_diameter = left_height + right_height

        # Update the max diameter
        max_diameter[0] = max(max_diameter[0], current_diameter)

        # height of a node = 1 + max(left_height, right_height) -> this is use to calculate a diameter
        return 1 + max(left_height, right_height)
    
    maxDiameter(root)
    return maxDiameter[0]

def invertTree(self, root):
    # base case
    if root == None:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
    invertTree(root.left)
    invertTree(root.right)
    return root

def isSubTree(self, root, subRoot):
    if not root and not subRoot or not subRoot:
        return True
    if root.val == subRoot.val:
        return isSameTree(root, subRoot)
    return isSubTree(root.left, subRoot.left) or isSubTree(root.right, root.left)

def isSameTree(self, root, subRoot):
    if not root and subRoot:
        return True
    if not root or not subRoot or root.val != subRoot.val:
        return False
    return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)

from collections import deque
def rightSideView(self, root):
    result = []
    queue = deque([root])

    while queue:
        # this is the variable to be added to the results
        rightSide = None
        # queue length allows you to pop exactly as many elements out of the queue as you have
        queue_length = len(queue)
        for i in range(queue_length):
            # parent, will be updated as we loop through the queue.  The rightSide variable, and what we ultimately want, will only be updated when you reach a non-null node
            parent = queue.popleft()
            # You may have null nodes, if so, don't account for them and, because of the conditional after the loop, it won't be added to the results
            if parent:
                # If the root/parent popped is non-null, assign that to your right side
                rightSide = parent
                # apppend the children of the node to the queue
                deque.append(parent.left)
                deque.append(parent.right)
        # update the rightSide variable ONLY when you have a non-null node
        if rightSide:
            result.append(rightSide.val)
    return result


def levelOrder(self, root):
    results = []
    queue = deque([root])

    if not root:
        return []

    while queue:
        nodes_in_order = []
        parents = []
        for parent in range(len(queue)):
            parent = queue.popleft()
            nodes_in_order.append(parent.val)
            parents.append(parent)
        for parent in parents:
            if parent.left:
                queue.append(parent.left)
            if parent.right:
                queue.append(parent.right)
        results.append(nodes_in_order)
    return results


def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def helper(root, lower_bound = float('-inf'), upper_bound = float('inf')):
        if not root:
            return True
        if not (root.val > lower_bound and root.val < upper_bound):
            return False
        return helper(root.left, lower_bound, root.val) and helper(root.right, root.val, upper_bound)
    return helper(root)

def kthSmallest(self, root, k):
    nodes_seen = []
    nodes_in_order = []
    def helper(root):
        # once you've passed the last node on the path, go back up 
        if not root:
            return
        # append the root you've visited
        nodes_seen.append(root)
        # traverse left.  You will traverse left until until you can't move left 
        helper(root.left)
        # the last value in the list is "the furthest left" node, which is the smallest node seen, at that time.  
        # It's not necessarily the bottom left node, it's simply the node that's furthest left at that point of time
        nodes_in_order.append(nodes_seen.pop())
        # move right
        helper(root.right)
        # return all the nodes in order
        return nodes_in_order
    return helper(root)[k-1].val

def buildTree(self, preorder, inorder):
    # the first value of the pre-order traversal is always the root
    root = preorder[0]
    # the position of the root in the in-order traversal is the divider of all nodes in the left tree vs in the right tree
    # thus, we need to find this position in each iteration to determine what will be in the left and right trees
    root_index = inorder.index(root)
    # everything from the root after the root to the index of the root in the pre-order traversal is in the left side of the tree 
    # everything in the left tree will be on the left side of the root in the in-order traversal
    root.left = self.build(preorder[:root_index + 1], inorder[:root_index])
    root.right = self.build(preorder[root_index + 1:], inorder[root_index +1:])
    return root

def maxPathSum(selr, root):
    result = [root.val]

    def helper(root):
        if not root:
            return 0
        # return: the value of the max path if we were to split at the node and thus you need the max paths of the left and right subtrees, recursively
        # compute: max sum splitting at the current root
        max_path_left = helper(root.left)
        max_path_right = helper(root.right)
        # nodes can be negative and thus we do not want to add them to our path's sum if that is the case
        max_path_left = max(max_path_left, 0)
        max_path_right = max(max_path_right, 0)
        
        # compute max path with splitting
        result[0] = max(result[0], root.val + max_path_left, max_path_right)

        # max path NOT splitting = root.val + max_path_left + max_path_right
        return root.val + max(max_path_left, max_path_right)
    
    helper(root)
    return result[0]

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        string = ''
        result = []
        def helper(root, string):
            if root == None:
                # when you reach the bottom, you've found a null node, add "N" for null
                string += "N,"
                result.append("N")
                return string
            string += f'{int(root.val)},'
            result.append(int(root.val))
            helper(root.left)
            helper(root.right)
            return string
        helper(root)
        return ",". join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # incoming data is a string delimited by commas
        vals = data.splt(',')
        # posiition is going to start at 0 => first value in the new vals array 
        self.i = 0
        def dfs():
            # base case of finding an encoded Null value => empty tree or end of the tree
            if vals[self.i] == 'N':
                # increment i
                self.i += 1
                return None
            # create root node for current subtree
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
