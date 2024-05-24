# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.




nums1 = [3,4,5,1,2]
# Output: 1

nums2 = [4,5,6,7,0,1,2]
# Output: 0

nums3 = [11,13,15,17]
# Output: 11

nums4 = [3,1,2]



def min_in_sorted_rotated(nums):
    left = 0 
    right = len(nums) - 1
    min_value = nums[0]
    while left <= right:
        if nums[left] < nums[right]:
            return min(min_value, nums[left])
        mid_point = (right + left) // 2
        min_value = min(min_value, nums[mid_point])
        if nums[left] <= nums[mid_point]:
            left = mid_point + 1
        else:
            right = mid_point - 1

    return min_value

print(min_in_sorted_rotated(nums4))