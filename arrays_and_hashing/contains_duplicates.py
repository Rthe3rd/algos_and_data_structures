class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        check_set = set()
        for num in nums:
            if num in check_set:
                return True
            check_set.add(num)
        return False 