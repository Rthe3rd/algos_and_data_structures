class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # base case empty tree/end of tree -> if root == None: return None

        # return value (parent to child) -> return a node and it's subsequent subtree
        # state to pass (child to parent) -> child node to recurse on and the VALUE you are deleting -> this will change!

        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            # four cases however case 1 is taken care of by 2 (or 3 depending on how you order the conditionals): 
              # 1. left/right subtree of root are empty
              # 2. left subtree is empty
              # 3. right subtree is empty
              # 4. left/right subtree are not empty
              if not root.left:
                  root = root.right
              elif not root.right:
                  root = root.left
              else:
                  current = root.right
                  while current.left:
                      current = current.left
                  
                  root.val = current.val
                  root.right = self.deleteNode(root.right, root.val)
        return root