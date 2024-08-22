from collections import deque
def zigzagLevelOrder(root):
    if not root:
        return []
    results = []
    deque = deque([root])
    # the deque strucutre allows you to add and take away in a First In First Out manner, which is needed for level order traversal
    while deque:
        # at the start of each loop, you want a fresh array to build the current level you are at on the tree
        level_to_build = []
        # the deque will be mutating during the foor loop, take a "snapshot" with len(deque)
        # this allows you to use a simple iterator of integers inside the deque instead of deque of lists
        for parent in range(len(deque)):
            # evaluate each parent in the deque 
            parent = deque.popleft()
            # add the parents to the level being built
            level_to_build.append(parent.val)
            # add the children that exist to the deque.  They will be the parents 
            if parent.left:
                deque.append(parent.left)
            if parent.right:
                deque.append(parent.right)
        # reverse the neccesary levels
        level_to_build = reversed(level_to_build) if len(results) % 2 == 1 else level_to_build
        # append the level_to_build to the results
        results.append(level_to_build)
    return results