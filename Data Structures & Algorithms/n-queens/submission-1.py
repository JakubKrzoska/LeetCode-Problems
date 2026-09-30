class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diagPos = set()
        diagNeg = set()

        res = []
        board = [["."]*n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
            
            for i in range(n):
                if i in cols or (i + r) in diagPos or (i - r) in diagNeg:
                    continue

                cols.add(i)
                diagPos.add(i + r)
                diagNeg.add(i - r)
                board[r][i] = "Q"

                backtrack(r + 1)

                cols.remove(i)
                diagPos.remove(i+r)
                diagNeg.remove(i-r)
                board[r][i] = "."

        backtrack(0)
        return res



