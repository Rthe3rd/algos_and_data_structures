# Given a list of unique integers, and a target, generate all the COMBINATIONS, that sum to the target


def combination_sum(nums, target):
    results = []
    current_combo = []

    def dfs_helper(index, current_combo, current_sum):
        # base cases
        # If target is met
        if current_sum == target:
            results.append(current_combo.copy())
            return
        # If the current sum is greater than the target OR if the index is out of bounds
        if index >= len(nums) or current_sum > target:
            return
        # Since we've made it past the base cases, it's time to make our two decsisions
        
        # Branch 1: add the value at the current index
        current_combo.append(nums[index])
        # Now call the dfs_helper on the current index => this branch will continually add the current value but splits on the next function call! 
        dfs_helper(index, current_combo, current_sum = current_sum + nums[index])
    
        # Branch 2: we do not want to add the value at the current index.  This prevents creating duplicates.  
        current_combo.pop()
        dfs_helper(index + 1, current_combo, current_sum)
    # call the function with the initial values
    dfs_helper(0, current_combo, 0)
    return results

print(combination_sum(nums = [2,3,6,7], target = 7))
print(combination_sum(nums = [2,3,5], target = 8))