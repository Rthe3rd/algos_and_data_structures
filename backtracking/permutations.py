def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # results = []
    # current_combo = []
    # Case 1: You have an empty tree
    if not nums:
        return [[]]

    # perms = self.permute(nums[1:])
    perms = permute(nums[1:])
    results = []

    for p in perms:
        for i in range(len(p) + 1):
            p_copy = p[:]
            p_copy.insert(i, nums[0])
            results.append(p_copy)
    return results


    # def dfs_helper(i):
    #     # base cases
    #     # Case 2: If our index is out of bounds
    #     if current_combo == len(nums):
    #         results.append(current_combo[:])
    #         return
        
    #     popped_val = nums.pop(0)
    #     current_combo.append(popped_val)

    #     dfs_helper(i)
    #     current_combo.pop()
    #     nums.append(popped_val)
        
    #     dfs_helper(i)

    # dfs_helper(0)
    # return results

print(permute(nums = [1,2,3]))