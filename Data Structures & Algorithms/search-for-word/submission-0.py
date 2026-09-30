class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(i, r, c):
            if i == len(word):
                return True
            if (min(r, c) < 0 or r == ROWS or c == COLS
                or board[r][c] != word[i] or (r, c) in visited):
                return False
            
            visited.add((r, c))
            res = (dfs(i + 1, r + 1, c) or
                   dfs(i + 1, r - 1, c) or 
                   dfs(i + 1, r, c + 1) or
                   dfs(i + 1, r, c - 1))
            visited.remove((r, c))
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(0, i, j):
                    return True
        return False


