from collections import defaultdict

# Validate sudoku board!
# Row/column is valid if 1-9 do not repeat
# 3x3 block (9 total) is valid if 1-9 do not repeat
# A partially filled board can be valid (i.e., has not yet broken validity constraints)

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

# Check this row (a list) for validity by seeing that 1-9 do not appear more than once
def row_validate(row):
    d = defaultdict(int)
    for item in row:
        if item != '.':
            d[item] += 1
        if d[item] > 1:
            print("Row failed: ", row)
            return False
    return True

# Convenience method that simply calls row_validate
def col_validate(col):
    return row_validate(col)

def block_validate(board, block_row, block_col):
    d = defaultdict(int)
    for i in range(3):
        for j in range(3):
            item = board[i + block_row*3][j + block_col*3]
            if item != '.':
                d[item] += 1
            if d[item] > 1:
                return False

# Create a list of all the elements in the ith column
def get_col(board, col_num):
    col = []
    for row in board:
        col.append(row[col_num])
    return col
    
# Validate all rows, then all columns, then all nine 3x3 blocks
def isValidSudoku(board) -> bool:

    # Validate each row
    for row in board:
        if row_validate(row) == False:
            return False
    
    # Grab column i and validate it 
    for i in range(9):
        col = get_col(board, i)
        if col_validate(col) == False:
            return False
    
    # Validate all 3x3 blocks
    for i in range(3):
        for j in range(3):
            if block_validate(board, i, j) == False:
                return False
            
    # If validation hasnt failed on anything, return True
    return True

print(isValidSudoku(board))
