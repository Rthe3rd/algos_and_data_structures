# Permutations of an array
# [1, 2 ,3] => [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]

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

def permute_dfs(nums):
    if not nums:
        return []

    results = []
    current_perm = []
    def dfs():
        if len(current_perm) == len(nums):
            results.append(current_perm[:])
            return

        for value in nums:
            if value not in current_perm:
                current_perm.append(value)
                dfs()
                current_perm.pop()
    dfs()
    return results 

print(permute_dfs(nums = [1,2,3]))

# This is a redo
def permutations(nums):
    results = []
    current_path = []
    used_vals = set()

    def dfs():
        if len(current_path) == len(nums):
            results.append(current_path.copy())
            return

        for val in nums:
            if not val in used_vals:
                current_path.append(val)
                used_vals.add(val)
                dfs()
                current_path.pop()
                used_vals.remove(val)

    dfs()
    return results

print(permutations(nums = [1,2,3]))