class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for i in range(n)]
        res = []

        col = set()
        posDiag = set() # (r + c) all values or r + c stay the same in right diagonal
        negDiag = set() # (r - c) all values or r - c stay the same in right diagonal

        # for every row, we check the columns positive diagonal and negative diagonal
        def backtrack(r):
            if r == n:
                # create the array into a string without any separators
                temp = [''.join(row) for row in board]
                res.append(temp)
                return
            # check the column locations of Queens for the previous rows
            for c in range(n):
                # check col, right diagonal and left diagonal
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                # this is the backtracking part where we consider other positions
                # so we go back and erase the current version of solution in this row
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'
        backtrack(0)
        return res
