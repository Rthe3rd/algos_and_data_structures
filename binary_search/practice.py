# Binary Search

def binary_search(input_array, target):
    left = 0
    right = len(input_array) - 1

    while left <= right:
        mid_point_of_array = (right + left)//2
        if target == input_array[mid_point_of_array]:
            return mid_point_of_array
        if target < input_array[mid_point_of_array]:
            right = target - 1
        if target > input_array[mid_point_of_array]:
            left = mid_point_of_array +1
    return -1


print(binary_search([1,4,3,2,6,5,8,9], 8))