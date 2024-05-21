# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
import math

def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    middle = 0

    while left <= right:
        middle = (right + left)//2
        if(nums[middle] == target):
            return middle
        if(nums[middle] > target):
            right = middle - 1 
        if(nums[middle] < target):
            left = middle + 1 
    else:
        return -1

