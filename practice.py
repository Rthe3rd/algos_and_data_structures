import time
def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    location_in_nums1 = 0
    for integer in nums2:
        print(integer)
        while integer > nums1[location_in_nums1] and nums1[location_in_nums1] != 0:
            location_in_nums1 += 1
        if location_in_nums1 == 0:
            print("here")
            nums1 = [integer, nums1[1:-1]]
        elif location_in_nums1 == len(nums1) - 1:
            nums1[-1] = integer
        else:
            nums1 = [*nums1[0:location_in_nums1], integer, *nums1[location_in_nums1 + 1:]]
    return nums1


# print(merge([1,2,3,4,5,0,0,0], 8, [8,9,10], 3))

def timer(n):
    start_time = time.time()
    non_count = [0]
    memoizer = {'1': 1, '2': 1}
    def fib(n):
        if memoizer[n] is not None:
            return memoizer[n]
        memoizer[str(n)] = fib(n-2) + fib(n-1)
        # result = memoizer[str(n-2)] + memoizer[str(n-1)]
        return memoizer[n]
    return fib(n)
    # return f'Total time: {time.time() - start_time} seconds. \nTotal Iterations: {non_count[0]}'

# print(timer(5))

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    results = []
    ordered_strs = {}
    for string in strs:
        sorted_string = "".join(sorted(string))
        if sorted_string not in ordered_strs:
            ordered_strs[sorted_string] = [string]
        else:
            ordered_strs[sorted_string].append(string)
    for key, value in ordered_strs.items():
        results.append(value)
    return results

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


def topKFrequent(nums, k):
    results = []
    # counts = [[]] * (len(nums) + 1)
    counts = [[] for i in range(len(nums) + 1)]
    freq_hash = {}
    for val in nums:
        freq_hash[val] = 1 + freq_hash.get(val, 0)
    for key, value in freq_hash.items():
        counts[value].append(key)
    # return counts
    for i in range(len(nums) - 1, -1, -1):
        if counts[i]:
            for val in counts[i]:
                results.append(i)
                if len(results) == k:
                    return results

# print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # left and right pointers
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid_point = (right + left) // 2
        if nums[mid_point] == target:
            return mid_point
        elif nums[mid_point] < target:
            # move left pointer
            left = mid_point + 1
        else:
            right = mid_point - 1
    return - 1

# print(search(nums = [-1,0,3,5,9,12], target = 9))
# print(search(nums = [-1,0,3,5,9,12], target = 2))

def searchMatrix(matrix, target):
    lower = 0
    upper = len(matrix[0]) - 1
    target_val_row_index = -1
    target_row = []
    if target > matrix[-1][-1] or target < matrix[0][0]:
        return False
    for row_index, row in enumerate(matrix):
        if target > matrix[row_index][0] and target < matrix[row_index][-1]:
            target_val_row_index = row_index
            target_row = row
        if target == matrix[row_index][0] or target == matrix[row_index][-1]:
            return True

    if target_val_row_index == -1:
        return False
    
    left = 0
    right = len(matrix[target_val_row_index]) - 1
    while left <= right:
        mid_point = (right + left) // 2
        mid_val = target_row[mid_point]
        if mid_val == target:
            return True
        elif target < mid_val:
            right = mid_point - 1
        elif target > mid_val:
            left = mid_point + 1
    return False

# print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
# print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
# print(searchMatrix(matrix = [[1,1]], target = 2))

import math
def minEatingSpeed(piles, h):
    # the max rate it could be is the largest value in the list i.e. the biggest pile of bananas
    max_rate = max(piles)
    # the fastest time the bananas could be ate in is math.ciel(len(piles)/max_rate)
    # the slowest rate it could be is 1 banana per hour
    min_rate = 1
    # using these, apply binary search on the range of rates on the largest pile
    right = max_rate
    left = 1
    min_rate = max_rate
    while left <= right:
        # for i in range(left, right + 1):
        # mid_index = (right + left) // 2
        mid_rate = (right + left) // 2
        # calculate the time to eat all the bananas
        total_time_to_eat = 0
        for index, number_of_bananas in enumerate(piles):
            time_to_eat_current_pile = math.ceil(number_of_bananas / mid_rate)
            total_time_to_eat += time_to_eat_current_pile
            # if the time it takes to eat the bananas at the given rate is less than the hours in which the keeprs will return 
        if total_time_to_eat > h:
            left = mid_rate + 1
        elif total_time_to_eat < h:
            right = mid_rate - 1
        else:
            min_rate = min(min_rate, mid_rate)
            right = mid_rate - 1
    return min_rate

print(minEatingSpeed(piles = [3,6,7,11], h = 8))
print(minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print(minEatingSpeed(piles = [30,11,23,4,20], h = 6))