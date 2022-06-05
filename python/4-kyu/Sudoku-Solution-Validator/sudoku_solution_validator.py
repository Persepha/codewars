def get_subgrid(board, row, column):
    subgrid = []
    for i in range(3):
        subgrid.extend(board[row + i][column:column+3])
    return subgrid

def is_valid(block):
    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    return not (digits - set(block))

def is_subgrids_valid(board):
    for i in range(3):
        for j in range(3):
            if not is_valid(get_subgrid(board, i*3, j*3)):
                return False
    return True

def is_rows_valid(board): 
    for row in board:
        if not is_valid(row):
            return False
    return True


def is_columns_valid(board):
    for index, x in enumerate(board):
        if not is_valid(row[index] for row in board):
            return False
    return True

def valid_solution(board):
    return is_subgrids_valid(board) and is_columns_valid(board) and is_rows_valid(board)
