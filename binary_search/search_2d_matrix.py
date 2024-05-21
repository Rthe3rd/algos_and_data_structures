# 74. Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

def search_2d_matrix(matrix, target):

    left_row = 0
    left_column = 0
    right_row = len(matrix) - 1
    right_column = len(matrix[0]) - 1
    # two binary searches, one for the rows, then one for the row that contains the value
    # log m + log n

    while left_column <= right_column and left_row <= right_row: 
        middle_row = (left_row + right_row) // 2    
        middle_column = (left_column + right_column) // 2
        print(middle_row, middle_column)
        if target == matrix[middle_row][middle_column]:
            return True
        
        if target < matrix[middle_row][right_column]:
            right_row = middle_row - 1
            # right_column = middle_column - 1

        if target > matrix[left_row][middle_column]:
            # left_row = middle_row + 1
            left_column = middle_column + 1

    return False

matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3

matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target2 = 13

print(search_2d_matrix(matrix2, target2))