# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation. 
import math

def except_self(nums):
    
    len_input_array = len(nums)
    ans = [1]*len_input_array
    prefix = 1
    for index in range(len_input_array):
        ans[index] = prefix
        prefix *= nums[index]

    postfix = 1
    for index in range(len_input_array - 1, -1, -1):
        ans[index] *= postfix
        postfix *= nums[index]
    return ans


print(except_self([1,2,3,4]))