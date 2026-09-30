class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, pDiag, nDiag = set(), set(), set()
        res = []
        board = [["." for i in range(n)] for  _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r - c) in nDiag or (r + c) in pDiag:
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                pDiag.add(r + c)
                nDiag.add(r - c)

                backtrack(r + 1)

                board[r][c] = "."
                cols.remove(c)
                pDiag.remove(r + c)
                nDiag.remove(r - c)

        backtrack(0)
        return res
            