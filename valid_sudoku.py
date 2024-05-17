# values are given by board[i][j] where "i" is the row and "j" is the column
# for i in range len(board)
# for j in range len(board)
# what is valid?
# row validity: All unique values across a row. Only 1 - 9 or '.' are valid
# column validity: All unique values across a column. Only 1 - 9 or '.' are valid
# 3 x 3 validity: All unique values within a 3 x 3 square: only 1 - 9 or '.' are valid
# How can these be validated?  
    # DS: Sets are efficient checkers if a number is in a collections, same with dictionaries
    # rows: board[iterating_value][fix_value]
    # columns: board[fix_value][iterating_value]
    # squares: board[i][j]:board[i+2][j], board[i][j]:board[i][j+2]
import collections 

def valid_sudoku(board):
    columnSet = collections.defaultdict(set)
    rowSet = collections.defaultdict(set)
    subGridSet = collections.defaultdict(set) # key will be a pair of values (row // 3, column // 3)

    # each value in the iterator is a constant row so this iterates by row
    for row in range(9):
        # each "column" is a different column. thus each loop, loops through each column of a given row  
        for column in range(9):
            # '.' == blank, go to next "column"
            if board[row][column] == ".":
                continue
            # check each value of the board to see if it already is in any of the checking "dict(set)"'s 
            if board[row][column] in rowSet[row] or board[row][column] in columnSet[column] or board[row][column] in subGridSet[ (row//3, column//3) ] :
                return False
            # add each value to each checking dict(set)
            columnSet[column].add(board[row][column])
            rowSet[row].add(board[row][column])
            # (row // 3 , column // 3) is the key to checking the subgrids.  
            # Each subgrid definied by "(row, column)" will be a key in a dictionary 
                # row/column = 0:2 => (row/column) // 3 = 0
                # row/column = 3:5 => (row/column) // 3 = 1 
                # row/column = 6:8 => (row/column) // 3 = 2 
            subGridSet[(row // 3, column // 3)].add(board[row][column])
    return True

board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# print(valid_sudoku(board1))
print(valid_sudoku(board2))