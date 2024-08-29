def setZeroes(self, matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # outer loop
    for row_index in range(len(matrix)): 
        for column_index in range(len(matrix[row_index])):
            # if current value == 0 => change the row/column values to "-" only if current values are not already 0
            if matrix[row_index][column_index] == 0:
                # flip the row
                for i in range(len(matrix[row_index])):
                    if matrix[row_index][i] != 0:
                        matrix[row_index][i] = '-'
                # flip the column
                for j in range(len(matrix)):
                    if matrix[j][column_index] != 0:
                        matrix[j][column_index] = '-'

    for row_index in range(len(matrix)): 
        for column_index in range(len(matrix[row_index])):
            if matrix[row_index][column_index] == '-':
                print('found dash')
                matrix[row_index][column_index] = 0
    return matrix

print(setZeroes(1, matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))  