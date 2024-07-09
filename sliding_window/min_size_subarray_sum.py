def minSubArrayLen(target, nums):
    # 
    left = 0
    running_sum = nums[left]
    right = 1
    min_length = len(nums) + 1
    if nums[left] >= target:
        return 1
    while right < len(nums):
        running_sum += nums[right]
        while running_sum >= target:
            min_length = min(right-left+1, min_length)
            running_sum -= nums[left]
            left += 1
        right += 1
    return 0 if min_length > len(nums) else min_length

target1 = 7
nums1 = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

target2 = 4
nums2 = [1,4,4]
# Output: 1

target3 = 11
nums3 = [1,1,1,1,1,1,1,1]
target3 = 7
nums3 = [8]
# Output: 0

print(minSubArrayLen(target1, nums1))
print(minSubArrayLen(target2, nums2))
print(minSubArrayLen(target3, nums3))
