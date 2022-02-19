import numpy as np


sudoku = input("Enter Sudoku")
# Un exemple de problème à entrer : 070000009510420600080300700008001370023080040400900100962800030000010400700203096


puz = np.array([[int(sudoku[(i+j)-1]) for i in range(1,10)] for j in range(0,81,9)])



def check(puzzle, i, row, col):
    rows = puzzle[int(row)]
    column = [puzzle[r][col] for r in range(0,9,1)]
    if i in rows:
        return False
    if i in column:
        return False
    SquareRow = (row // 3)*3
    squareColumn = (col // 3)*3
    Square = [puzzle[y][z] for y in range(SquareRow, SquareRow+3) for z in range(squareColumn, squareColumn+3)]
    if i in Square:
        return False
    return True


def find(puzzle):
    for i in range(0,9,1):
        for j in range(0,9,1):
            if puzzle[i][j]==0:
                return i,j
    return None


def solve(board):
    finds = find(board)
    if not finds:
        return True
    else:
        row, col = finds

    for i in range(1,10):
        if check(board, i, row, col):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


print(puz)
print(solve(puz))
print(puz)
