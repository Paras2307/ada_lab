from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    result = []
    board = [['.'] * n for _ in range(n)]

    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return

        for col in range(n):
            safe = True

            for r in range(row):
                if board[r][col] == 'Q':
                    safe = False
                    break

                if abs(row - r) == abs(col - next(
                    c for c in range(n) if board[r][c] == 'Q'
                )):
                    safe = False
                    break

            if safe:
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)
    return result


print("solveNQueens(4):", solveNQueens(4))