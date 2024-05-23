# check_set built from the input array 
#  
import math


def longest_sequence(nums):
    # make a set from the array of numbers
    check_set = set(nums)
    max_length = 1
    # loop through each of the numbers
    for number in nums:
        # check to see if there is a smaller number in the set, 
        # if there is NOT a smaller number, increase the "current_number" by one and check the set each time, increasing the max length each time
        if number - 1 not in check_set:
            current_length = 1
            while number + 1 in check_set:
                number += 1
                current_length += 1
            if current_length > max_length:
                max_length = current_length
        # if there is, this can't be the *start* of a sequence
    return max_length

print(longest_sequence([1,2,3,4,56]))
            