class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        integers_and_indices = {}
        for index in range(len(nums)):
            if target - nums[index] in integers_and_indices:
                return [index, integers_and_indices[target - nums[index]]]
            if nums[index] not in integers_and_indices:
                integers_and_indices[nums[index]] = index
        return []