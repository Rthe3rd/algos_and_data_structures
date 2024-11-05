# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

import collections
def permuteUnique(self, nums: list[int]) -> list[list[int]]:
    result = []
    current_path = []

    # This is the "pruning function".  
    counter = collections.Counter(nums)

    def dfs():
        # Leaf node
        if len(current_path) == len(nums):
            result.append(current_path.copy())
            return
        
        # This is in effect is the pruning function, each num is unique do to translating the input array to a hash!
        for num in counter:
            if counter[num] > 0:
                current_path.append(num)
                counter[num] -= 1
                # Each dfs call is a branch in the recursion tree
                dfs()
                # After the call to DFS, you are essentially going back up to the most recent split/branching of the tree, 
                # Each branch/splitting of the tree means adding a num to the permutation
                # thus you need to +=1 the count for the number previously added as you're going down a new branch
                # Popping is doing exctly this
                current_path.pop()
                counter[num] += 1

    dfs()
    return result
