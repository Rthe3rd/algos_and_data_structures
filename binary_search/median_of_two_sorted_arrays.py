def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # merge ordered list
        # find median?
        left1 = 0
        left2 = 0
        merged_nums = []
        while left1 < len(nums1) and left2 < len(nums2):
            print(f'left1: {left1}')
            print(f'left2: {left2}')
            if nums1[left1] < nums2[left2]:
                merged_nums.append(nums1[left1])
                left1 += 1
            elif nums1[left1] >= nums2[left2]:
                merged_nums.append(nums2[left2])
                left2 += 1
        while left1 < len(nums1):
            merged_nums.append(nums1[left1])
            left1 += 1
        while left2 < len(nums2):
            merged_nums.append(nums2[left2])
            left2 += 1 

        left = 0
        right = len(merged_nums) - 1
        if len(merged_nums) == 0:
            return []
        if len(merged_nums) == 1:
            return merged_nums[0]
        if len(merged_nums) == 2:
            return (merged_nums[0] + merged_nums[1])/2
        if len(merged_nums) % 2 == 0:
            while left + 1 != right:
                left += 1
                right -= 1
            return (merged_nums[left] + merged_nums[right])/2
        while left != right:
            left += 1
            right -= 1
            return (merged_nums[left] + merged_nums[right])/2
        return merged_nums

            
nums1 = [1,3]
nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

nums3 = [1,2]
nums4 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

print(findMedianSortedArrays(nums1, nums2))
print(findMedianSortedArrays(nums3, nums4))