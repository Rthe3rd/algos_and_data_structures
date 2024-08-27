def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    # m x n matrix => rows "m" by columns "n"
    # location on board = board[row][column]
    #   row = board[0:len(board)][constant_value]
    #   column = board[contant_value][0:len(board[0])]
    
    # things to keep track of:
    #   Where you are: out of bounds: 
    #       Rows "m": 0 <= i < m 
    #       Columns "n": 0 <= j < n 
    #   Where you've been => can't go to the same place twice/can't backtrack on yourself => how do you keep track of this? hash set of coordinate pairs?
    #   current string you are building

    # Moving: step left, step right, step up, step down => from position board[i][j]
    #   step_left = board[i][j-1]
    #   step_right = board[i][j+1]
    #   step_up = board[i+1][j]
    #   step_down = board[i-1][j]

    # Method Type: Recursive with a DFS traversal
    # Base cases:
    #   Out of bounds or "you've already been there" or the length of the string is longer than the string you ar e looking for
    
    # REFRAMING PROBLEM: Since we don't need to actually build the word, we can just go until we've matched all letters or we hit base cases 

    def dfs_helper(i, j , current_word_index):
        if current_word_index == len(word):
            return True
        # If the letter we are at does not match the letter in the string, return false
        if( i < 0 or i >= len(board) 
            or j < 0 or j >= len(board[0]) 
            or board[i][j] != word[current_word_index]
            or (i,j) in check_set):
            return False

        check_set.add((i,j))
        # take all possible steps
        # if any return true, return true
        result = (
            dfs_helper(i+1, j, current_word_index + 1) 
            or dfs_helper(i-1, j, current_word_index + 1)
            or dfs_helper(i, j+1, current_word_index + 1) 
            or dfs_helper(i, j-1, current_word_index + 1)
        )
        # CRITICAL! This allows you to visit i,j from another path
        # Before using the next starting location, given by the loops, all of the previously values are removed from the set
        # You don't want to clear the entire path at once, only remove the last values as you find out that they are not viable paths
        check_set.remove((i,j))
        return result

    check_set = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs_helper(i, j, 0):
                return True
    return False
