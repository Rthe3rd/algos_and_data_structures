# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threeSum(input_array):
    # order array
    ordered_array = sorted(input_array)
    triplets = []
    # loop forward with a standard for loop
    # set two pointer indices:
        # left pointer: i + 1
        # right pointer: len(input_array) - 1
        # while the left pointer is to the left of the right pointer
        # if left + right + numbers[i] < 0 => move left pointer +=
        # elif left + right + numbers[i] < 0 => move right pointer -=
        # else: => add indicies to a results array
        # There are potentially more pairs that add up to 0, so move one of the pointers until it is not the same value
            # while numbers[left] == numbers[left + 1] => move left to the right
            # Once you reach a new value check to see if the sum is gerater than 0, if it is, exit loop, it is not, more the right pointer, 

    for i in range(0, len(ordered_array) - 1):
        # current_sum = ordered_array[i]
        left = i + 1
        right = len(ordered_array) - 1
        if i > 0 and ordered_array[i] == ordered_array[i - 1]:
            continue
        while left < right:
            sum = ordered_array[left] + ordered_array[right] + ordered_array[i]
            if sum < 0:
                left += 1
            elif sum> 0:
                right -= 1
            else:
                triplets.append([ordered_array[left], ordered_array[right], ordered_array[i]])
                left += 1
                while ordered_array[left] == ordered_array[left-1] and left < right:
                    left += 1
    return triplets

# Example 1:
nums1 = [-1,0,1,2,-1,-4]
# [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
nums2 = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
nums3 = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

print(threeSum(nums1))