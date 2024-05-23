# 74. Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

def search_2d_matrix(matrix, target):
    # two binary searches, one for the rows, then one for the row that contains the value
    # log m + log n

    # Time complexity: O(m)
    # Get the target_row
    right_column = len(matrix[0]) - 1 
    target_row_index = -1
    for row_index, row in enumerate(matrix):
        if target >= row[0] and target <= row[right_column]:
            target_row_index = row_index
            target_row = row
    if target_row_index == -1:
        return False
    left = 0 
    right = len(matrix[0]) - 1

    # Time complexity: O(logn)
    while left <= right:
        mid_point_index = (right + left) // 2
        if target == target_row[mid_point_index]:
            return [target_row_index, mid_point_index]
        if target < target_row[mid_point_index]:
            right = mid_point_index - 1
        if target > target_row[mid_point_index]:
            left = mid_point_index + 1 

    return False

matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3

matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target2 = 23

matrix3 = [[1,3,5,7],[10,11,16,20],[23,30,34,60],[71,73,78,80]] 
target3 = 80

print(search_2d_matrix(matrix1, target1))
print(search_2d_matrix(matrix2, target2))