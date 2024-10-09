class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:

        # first set up the binary search template
        left, right = 0 , len(nums) - 1
        single_index = -1

        while left <= right:
            mid_point = (left + right) // 2
        # the non-paired integer splits the array into two different sections: before and after it's occurence
            # before it's occurence the first of two values appears on an EVEN index and the second appearence is on an ODD index
            # after it's occurence the first of paired values appears on an odd index and the second appearence is on an EVEN index
            # Using these two facts, we can determine how to move our bounds based on where we land with the mid_point idx and the values before/after

            if self.is_single_seen(mid_point, nums):
                single_index = mid_point
                right = mid_point - 1
            else:
                left = mid_point + 1

        return nums[single_index]

    def is_single_seen(self, mid_point, nums):
        # check if single value has been seen
            # if it has been seen, then even indices will have the same value ahead of it
        
        # 1. At the end of the array branch
        # if mid_point == len(nums) - 1:
        #     return True
        # # 2. Odd branch
        # if mid_point % 2 != 0:
        #     return nums[mid_point] != nums[mid_point - 1]
        # # 3. Even branch
        # else:
        #     return nums[mid_point] != nums[mid_point + 1]
        
        # 1. At the end of the array branch
        if mid_point == len(nums) - 1:
            return True
        # 2. Even branch
        elif mid_point % 2 == 0:
            return nums[mid_point] != nums[mid_point + 1]
        # 3. Odd branch
        else:
            return nums[mid_point] != nums[mid_point - 1]


print(Solution().singleNonDuplicate(nums = [1,1,2,3,3,4,4,8,8]))
# Output: 2

print(Solution().singleNonDuplicate(nums = [3,3,7,7,10,11,11]))
# Output: 10