#!/usr/bin/python3
"""Solves the N-queens puzzle
Determines all possible solutions to placing N."""


import sys


global N
N = 4


def print_board(board):
    """Printing the board."""
    board = []
    [board.append([]) for i in range(N)]
    [row.append(' ') for i in range(N) for row in board]
    return (board)

def add_sol(board, ans):
    tmp = []
    for i in range(N):
        string = ""
        for j in range(N):
            string += board[i][j]
        tmp.append(string)
    ans.append(tmp)


def is_safe(row, col, board):
    """Making sure Queen is safe."""
    x = row
    y = col
    while(x >= 0):
        if board[x][y] == "Q":
            return (False)
        else:
            x -= 1

    """Check upper right."""
    x = row
    y = col
    while(y < N and x >= 0):
        if board[x][y] == "Q":
            return (False)
        else:
            y += 1
            x -= 1
    """Check upper left."""
    x = row
    y = col
    while(y >= 0 and x >= 0):
        if board[x][y] == "Q":
            return (False)
        else:
            x -= 1
            y -= 1
    return (True)


def solveNQueens(row, ans, board, N):
    """Solving nqueens problem."""
    if row == N:
        add_sol(board, ans, N)
        return

    for col in range(N):
        if is_safe(row, col, board):
            board[row][col] = "Q"
            solution = solveNQueens(row+1, ans, board, N)
            board[row][col] = "."


if __name__ == "__main__":
    ans = []
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = print_board(int(sys.argv[1]))
    solutions = solveNQueens(0, ans, board, N)
    for sol in solutions:
        print(sol)
