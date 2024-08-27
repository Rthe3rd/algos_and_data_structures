def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = []
    subset = []
    checket_set = set()
    # sort list
    nums = sorted(nums)
    def dfs(i, current_subset = []):
        # this is the base case i.e. when you've already reached the last index
        if i == len(nums):
            results.append(subset[:])
            return

        # add current value to subet
        # all subsets that include nums[i]
        subset.append(nums[i])
        dfs(i + 1, subset)

        # The main difference between subset I and subset II is that instead of moving just one index, you move until you don't repeat characters
        # Note this only works since you have sorted the lsit
        # do not add current value
        # all subsets that DO NOT include nums[i]
        element_not_to_add = subset.pop()
        while i < len(nums) and nums[i] == element_not_to_add:
            i += 1
        dfs(i, subset)

    dfs(0)
    return results

print(subsetsWithDup(nums = [1,2,3]))
# print(subsetsWithDup(nums = [4,4,4,1,4]))