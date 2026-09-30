class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = set()

        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visited or grid[r][c] == 0):
                return 0

            visited.add((r, c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    res = max(res, dfs(i, j))
        return res