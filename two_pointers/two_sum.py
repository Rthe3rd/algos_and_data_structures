# Two Sum: Given an input array of numbers and a target, find the two indices of elements that add up to the target

def two_sum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left = 0
    right = len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum > target:
            right -= 1
        elif sum < target:
            left += 1
        else:
            return [left + 1, right + 1 ]  

input_array = [1,3,3,4]
target = 6
print(two_sum(input_array, target))