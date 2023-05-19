# Determine if a 9 x 9 Sudoku board is valid. 
# Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

def validSubBoxes(board):
   
    first_sub = [board[i][j] for i in range(3) for j in range(3) if board[i][j] != '.']
    second_sub = [board[i][j] for i in range(3) for j in range(3,6) if board[i][j] != '.']
    third_sub = [board[i][j] for i in range(3) for j in range(6,9) if board[i][j] != '.']
    fourth_sub = [board[i][j] for i in range(3,6) for j in range(3) if board[i][j] != '.']
    fifth_sub = [board[i][j] for i in range(3,6) for j in range(3,6) if board[i][j] != '.']
    sixth_sub = [board[i][j] for i in range(3,6) for j in range(6,9) if board[i][j] != '.']
    seventh_sub = [board[i][j] for i in range(6,9) for j in range(3) if board[i][j] != '.']
    eighth_sub = [board[i][j] for i in range(6,9) for j in range(3,6) if board[i][j] != '.']
    ninth_sub = [board[i][j] for i in range(6,9) for j in range(6,9) if board[i][j] != '.']

    return len(first_sub) == len(set(first_sub)) and len(second_sub) == len(set(second_sub)) and \
        len(third_sub) == len(set(third_sub)) and len(fourth_sub) == len(set(fourth_sub)) and \
        len(fifth_sub) == len(set(fifth_sub)) and len(sixth_sub) == len(set(sixth_sub)) and \
        len(seventh_sub) == len(set(seventh_sub)) and len(eighth_sub) == len(set(eighth_sub)) and \
        len(ninth_sub) == len(set(ninth_sub))

def validCol(board):

    for i in range(9):
        holder = []
        for j in range(9):
            if board[j][i] != '.':
                holder.append(board[j][i])
            
        if len(holder) != len(set(holder)):
            return False

    return True

def validRow(board):

    for i in range(9):
        holder = []
        for j in range(9):
            if board[i][j] != '.':
                holder.append(board[i][j])
        
        if len(holder) != len(set(holder)):
            return False

    return True

def isValidSudoku(board):

    if not validSubBoxes(board):
        print('sub_box')
        return False
    
    if not validCol(board):
        print('col')
        return False
    
    if not validRow(board):
        print('row')
        return False
    
    return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))