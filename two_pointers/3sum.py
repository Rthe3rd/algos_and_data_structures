# 3 Sum: Given an array of numbers and a target value, return the *all* the triplets of indices of the three numbers which 0:
# Random order 
# No duplicates

# initial thoughts, we need to keep track of the values seen and their indices alreay
# not 100% sure how two pointers comes in to play
# need to store sums? 
# build a structure of two sums doublets and then see if there are "target - value" in the two_set_structure/checker


def three_sum(input_array):
    triplets = []
    input_array = sorted(input_array)
    for i, element in enumerate(input_array):
        # because they're sorted, if there is a duplicate, it will be the next value
        # this is lieu of using a set to check
        # this is to check if you just have reached a duplicate, i.e. the previous value was the same for element: element = 2 AND element = 3, nums = [-4, 1, 1, 1, 3 ] 
        if i > 0 and element == input_array[i - 1]:
            continue
        left = i + 1
        right = len(input_array) - 1
        while left < right:
            sum = input_array[left] + input_array[right] + element
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                triplets.append([input_array[left], input_array[right], element])
                # There may be more than one pair of values that are the inverse of the current value ("element") and thus the pointers need to move
                # Move left or right, until they are not the same value as previous AND do not cross the other pointer 
                left += 1
                # this is to check if you just reached the end of a sequence of duplicates with left: left = 2, nums = [-4, 1, 1, 3 ] 
                while input_array[left] == input_array[left-1] and left < right:
                    left += 1
    return triplets


nums = [-1,0,1,2,-1,-4]
# nums = [0,0,0,0]
print(three_sum(nums))