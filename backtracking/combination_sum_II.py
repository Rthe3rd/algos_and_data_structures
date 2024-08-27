def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    
    # Combinations: 
    #   Order doesn't matter
    #   Values can only be used once
    # Things to keep track of:
    #   Current/running sum for a given index
    #   current_subset
    # Some sort of dfs
    #   How does the index move? i + 1? 
    #   Base cases: 
    #       current_sum == target => append current_subset
    #       current_sum > target OR index is out of bounds => return
    # How do you prevent duplicates?
    #   [1, 1, 2] and [1, 2, 1] => perhaps sorting the list beforehand?

    results = []
    current_combination = []
    candidates = sorted(candidates)

    def dfs_helper(i, current_sum):
        if current_sum == target:
            results.append(current_combination[:])
            return 
        if current_sum > target or i >= len(candidates):
            return

        current_combination.append(candidates[i])
        current_sum += candidates[i]
        dfs_helper(i + 1, current_sum)

        popped_value = current_combination.pop()
        current_sum -= popped_value
        while i < len(candidates) and candidates[i] == popped_value:
            i += 1
        dfs_helper(i, current_sum)

    dfs_helper(0, 0)
    return results

print(combinationSum2([2,5,2,1,2], 5))