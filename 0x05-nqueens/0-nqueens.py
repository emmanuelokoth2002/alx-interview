#!/usr/bin/python3
"""solves the N queens problem."""

import sys


def is_safe(board, row, col, N):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def solve_n_queens(N):
    solutions = []

    def solve(board, row):
        if row == N:
            solutions.append(list(board))
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve(board, row + 1)

    solve([0] * N, 0)
    return solutions


def print_solutions(solutions):
    for solution in solutions:
        print([[i, col] for i, col in enumerate(solution)])


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        solutions = solve_n_queens(N)
        print_solutions(solutions)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

if __name__ == "__main__":
    main()
