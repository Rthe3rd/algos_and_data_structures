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

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


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

# print(minEatingSpeed(piles = [3,6,7,11], h = 8))
# print(minEatingSpeed(piles = [30,11,23,4,20], h = 5))
# print(minEatingSpeed(piles = [30,11,23,4,20], h = 6))


def prefix(nums):
    prefix_sum = [0] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            prefix_sum[i] = nums[i]
        else:
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    prefix_product = [1] * len(nums)
    
    return prefix_sum

# [2, 4, 6, 8] => [2, 6, 12 , 20]
# print(prefix([2, 4, 6, 8]))

def max_subarray(nums):
    max_sum = nums[0]
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return max_sum

def max_subarray_two_pointer(nums):
    max_sum = nums[0]
    max_left, max_right = 0, 0
    current_sum = 0
    left = 0

    for right in range(len(nums)):
        if current_sum < 0:
            current_sum = 0
            left = right

        current_sum += nums[right]
        if current_sum > max_sum:
            max_sum = current_sum
            max_left, max_right = left, right

    return [max_left, max_right]

print(max_subarray_two_pointer([4, -1, 2, -7, 3, 4]))

def groupAnagrams(strs):
    check = {}
    result = []

    for string in strs:
        sorted_string = "".join(sorted(string))
        if not sorted_string in check:
            check[sorted_string] = [string]
        else:
            check[sorted_string].append(string)

    for key, value, in check.items():

        result.append(value)
    
    return result

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

from collections import Counter

def topKFrequent(nums, k):
    results = [[] for n in range(len(nums) + 1)]
    counter = {}
    kth_most = []

    for index, value in enumerate(nums):
        counter[value] = 1 + counter.get(value, 0)

    for integer, frequency in counter.items():
        results[frequency].append(integer)

    for index in range(len(results) -1, -1, -1):
        for val in results[index]:
            kth_most.append(val)
            if len(kth_most) == k:
                return kth_most

    return results

# print(topKFrequent([1,1,1,2,2,3], 2))
# print(topKFrequent([1, 1], 1))

def product_except_self(nums):
    prefix = [1] * len(nums)

    a = 1
    for i in range(1, len(nums)):
        prefix[i] *= nums[i-1] * a 
        a = prefix[i]

    b = 1
    for j in range(len(nums) - 1, -1 , -1):
        prefix[j] *= b
        b *= nums[j]

    return prefix

# print(product_except_self([1,2,3,4]))
# print(product_except_self([2,3,5,0]))

from collections import defaultdict
def valid_sudoku(matrix):
    row_checker = defaultdict(set)
    column_checker = defaultdict(set)
    subgrid_checker = defaultdict(set)

    for row in range(9):
        for column in range(9):
            current_val = matrix[row][column]
            if current_val == '.':
                continue
            if current_val in column_checker[column] or current_val in row_checker[row] or current_val in subgrid_checker[row//3,column//3]:
                return False
            row_checker[row].add(current_val)
            column_checker[column].add(current_val)
            subgrid_checker[row//3,column//3].add(current_val)



    # return subgrid_checker

# print(valid_sudoku([["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))

# print(valid_sudoku([["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))

import re
def isPalindrome(s: str) -> bool:
    # cleaned_s = re.findall(r'([a-z]+)', s.lower())
    # cleaned_s = "".join(cleaned_s)
    # left = 0
    # right = len(cleaned_s) - 1
    # while left <= right:
    #     if cleaned_s[right] != cleaned_s[left]:
    #         return False
    #     right -= 1
    #     left += 1
        lower_string = s.lower()
        new_string = ''
        for index, character in enumerate(lower_string):
            if (ord(character) >= ord('a') and ord(character) <= ord('z') or ord(character) >= ord('0') and ord(character) <= ord('9')):
                new_string += character
        return new_string == new_string[::-1]
        # return True

# print(isPalindrome("A man, a plan, a canal: Panama"))
# print(isPalindrome("race a car"))


def twoSum(self, numbers: int, target: int):
    left = 0
    right = len(numbers) - 1
    results = []

    while left <= right:
        two_sum = numbers[left] + numbers[right]
        if two_sum == target:
            return [left + 1, right + 1]
        if two_sum < target:
            left += 1
        if two_sum > target:
            right -= 1
    return [left, right]

