# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.


def search_sorted_rotated(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_point = (right + left) // 2
        if nums[mid_point] == target:
            return mid_point
        # Which portion of the array are we in? i.e. where is the value of the mid_point in terms of all the values? In the "left sorted" portion? "right sorted"?
        # if the left value is less than or equal to the value at the mid_point, the mid_point is in the "left sorted portion" of the array
        if nums[left] <= nums[mid_point]:
            # how do you decide which portion of the list to "binary search" on?
            # target < nums[left] =>  
            if target > nums[mid_point] or target < nums[left]:
                left = mid_point + 1
            # This means that the target is less than the middle but greater than the left most value => search the left portion of the array => move right pointer
            else:
                right = mid_point - 1
        # if the left value is greater than the value at the mid_point, the mid_point is in the "right sorted portion" of the array
        else:
            # since we are in the right sorted portion, values increase right to left
            # target < nums[mid_point] => value at the mid_point is larger than the target => search the left => move the right pointer
            # target > nums[right] => target value is greater than our than our right most/greatest value in the right sorted portion => search left (it's not in the right!) => more right pointer
            if target < nums[mid_point] or target > nums[right]:
                right = mid_point - 1
            # 
            else:
                left = mid_point + 1
    return -1



nums1 = [4,5,6,7,0,1,2]
target1 = 0
# Output: 4

nums2 = [4,5,6,7,0,1,2]
target2 = 3
# Output: -1

nums3 = [1]
target3 = 0

print(search_sorted_rotated(nums1, target1))
print(search_sorted_rotated(nums2, target2))