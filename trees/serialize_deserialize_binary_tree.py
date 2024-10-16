class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
    
        result = []

        def dfs(root):
            if not root:
                return result.append("N")
            result.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return root
        dfs(root)
        return "-".join(result)




    def deserialize(self, data):
        
        vals = data.splt("-")
        self.i = 0
        def helper():
            if vals[self.i] == '-':
                self.i += 1
                return None
            root = TreeNode(int(vals[self.i]))
            self.i += 1
            root.left = helper()
            root.right = helper()
            return root

        return helper()
