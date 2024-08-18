


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = []
    subset = []
    def dfs(i):
        # this is the base case i.e. when you've already reached the last indexb 
        if i == len(nums):
            # Leet code runs python version 2.xx so the copy(), and results.append(subset.copy()), don't work
            results.append(subset[:])
            # return nothing because we are building/appending to a global
            # we don't need any values to add to our recursive function calls
            return
        subset.append(nums[i])
        # recursively call the dfs until you reach the end of the list
        dfs(i + 1)
        # pop off the item last added.  This is equivalent to not adding something to your subset
        subset.pop()
        # recursively call dfs until you reach the end of the list
        dfs(i + 1)
    # call dfs with your first index => 0
    dfs(0)
    return results
print(subsets([1,2,3]))