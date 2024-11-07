#!/usr/bin/python3
"""
placing N non-attacking queens on an N×N chessboard
"""

import sys


def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, solutions):
    if col >= len(board):
        # Convert board to a solution format and add to solutions
        solution = []
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 1:
                    solution.append([row, col])
        solutions.append(solution)
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, solutions)
            board[i][col] = 0  # Backtrack


def solve_nqueens(N):
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    for solution in solutions:
        print(solution)


def main():
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
